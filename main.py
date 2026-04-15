import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from config import *
from data_preprocessing import generate_synthetic_data, load_and_preprocess_data, create_sequences, split_data
from train import train_model
from predict import load_trained_model, load_scaler, evaluate_predictions
from visualization import (
    plot_load_data, plot_training_history, 
    plot_predictions, plot_single_day_prediction, plot_correlation_matrix
)
import numpy as np
import matplotlib
matplotlib.use('Agg')

def main():
    print("=== Power Load Prediction Project ===")
    
    scaled_data, _ = load_and_preprocess_data()
    X, y = create_sequences(scaled_data)
    _, _, X_test, _, _, y_test = split_data(X, y)
    
    if not os.path.exists(MODEL_PATH):
        print("\n1. Training model...")
        model, scaler, _, _ = train_model()
    else:
        print("\n1. Loading trained model...")
        model = load_trained_model()
        scaler = load_scaler()
    
    print("\n2. Evaluating model...")
    rmse, mae, mape, y_test_actual, y_pred_actual = evaluate_predictions(model, X_test, y_test, scaler)
    print(f"RMSE: {rmse:.2f} MW")
    print(f"MAE: {mae:.2f} MW")
    print(f"MAPE: {mape:.2f}%")
    
    print("\n3. Generating visualizations...")
    
    df = generate_synthetic_data()
    corr_plt = plot_correlation_matrix(df)
    corr_plt.savefig(os.path.join(BASE_DIR, 'correlation_matrix.png'))
    corr_plt.close()
    print("Saved: correlation_matrix.png")
    
    history = np.load(os.path.join(MODEL_DIR, 'history.npy'), allow_pickle=True).item()
    history_plt = plot_training_history(history)
    history_plt.savefig(os.path.join(BASE_DIR, 'training_history.png'))
    history_plt.close()
    print("Saved: training_history.png")
    
    pred_plt = plot_predictions(y_test_actual, y_pred_actual)
    pred_plt.savefig(os.path.join(BASE_DIR, 'predictions.png'))
    pred_plt.close()
    print("Saved: predictions.png")
    
    y_pred_scaled = model.predict(X_test)
    day_plt = plot_single_day_prediction(y_test.reshape(-1, 24), y_pred_scaled.reshape(-1, 24))
    day_plt.savefig(os.path.join(BASE_DIR, 'single_day_prediction.png'))
    day_plt.close()
    print("Saved: single_day_prediction.png")
    
    print("\n=== Project completed successfully! ===")
    print(f"Model saved to: {MODEL_PATH}")
    print("Visualizations saved to project directory.")

if __name__ == '__main__':
    main()