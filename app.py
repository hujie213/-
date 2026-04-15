import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from flask import Flask, render_template, jsonify
import numpy as np
import pandas as pd
from config import *
from data_preprocessing import generate_synthetic_data, load_and_preprocess_data, create_sequences, split_data
from model import build_lstm_model
from predict import load_trained_model, load_scaler, inverse_transform_load, evaluate_predictions

app = Flask(__name__)

model = None
scaler = None
df = None

def init_model():
    global model, scaler, df
    
    df = generate_synthetic_data()
    scaled_data, _ = load_and_preprocess_data()
    X, y = create_sequences(scaled_data)
    
    if os.path.exists(MODEL_PATH):
        model = load_trained_model()
        scaler = load_scaler()
    else:
        X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
        input_shape = (X_train.shape[1], X_train.shape[2])
        model = build_lstm_model(input_shape)
        model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
        model.save(MODEL_PATH)
        scaler = load_scaler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    recent_data = df.tail(168)
    data = {
        'dates': recent_data.index.strftime('%Y-%m-%d %H:%M').tolist(),
        'load': recent_data['load'].tolist(),
        'temperature': recent_data['temperature'].tolist(),
        'humidity': recent_data['humidity'].tolist()
    }
    return jsonify(data)

@app.route('/api/predict')
def get_prediction():
    global model, scaler, df
    
    recent_data = df.tail(SEQ_LENGTH)
    recent_data = recent_data[FEATURE_COLS]
    
    scaled_input = scaler.transform(recent_data)
    seq = scaled_input.reshape(1, SEQ_LENGTH, len(FEATURE_COLS))
    scaled_pred = model.predict(seq)
    pred = inverse_transform_load(scaler, scaled_pred[0])
    
    last_date = df.index[-1]
    pred_dates = pd.date_range(last_date + pd.Timedelta(hours=1), periods=PREDICTION_HORIZON, freq='H')
    
    return jsonify({
        'dates': pred_dates.strftime('%Y-%m-%d %H:%M').tolist(),
        'prediction': pred.tolist()
    })

@app.route('/api/evaluate')
def get_evaluation():
    global model, scaler
    
    scaled_data, _ = load_and_preprocess_data()
    X, y = create_sequences(scaled_data)
    _, _, X_test, _, _, y_test = split_data(X, y)
    
    rmse, mae, mape, y_test_actual, y_pred_actual = evaluate_predictions(model, X_test, y_test, scaler)
    
    return jsonify({
        'rmse': float(rmse),
        'mae': float(mae),
        'mape': float(mape)
    })

@app.route('/api/forecast')
def get_forecast():
    global model, scaler, df
    
    recent_data = df.tail(168 + SEQ_LENGTH)
    actual_dates = recent_data.index.strftime('%Y-%m-%d %H:%M').tolist()
    actual_load = recent_data['load'].tolist()
    
    recent_features = recent_data[FEATURE_COLS]
    scaled_input = scaler.transform(recent_features)
    
    predictions = []
    current_seq = scaled_input[-SEQ_LENGTH:]
    
    for _ in range(PREDICTION_HORIZON):
        seq = current_seq.reshape(1, SEQ_LENGTH, len(FEATURE_COLS))
        scaled_pred = model.predict(seq)
        pred = inverse_transform_load(scaler, scaled_pred[0])
        predictions.extend(pred.tolist())
        
        new_row = np.zeros(len(FEATURE_COLS))
        new_row[0] = scaled_pred[0][-1]
        current_seq = np.vstack([current_seq[1:], new_row])
    
    last_date = df.index[-1]
    pred_dates = pd.date_range(last_date + pd.Timedelta(hours=1), periods=PREDICTION_HORIZON, freq='H')
    pred_dates_str = pred_dates.strftime('%Y-%m-%d %H:%M').tolist()
    
    return jsonify({
        'actual_dates': actual_dates,
        'actual_load': actual_load,
        'pred_dates': pred_dates_str,
        'pred_load': predictions[:PREDICTION_HORIZON]
    })

if __name__ == '__main__':
    init_model()
    app.run(host='0.0.0.0', port=5000, debug=True)