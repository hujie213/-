import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODEL_DIR = os.path.join(BASE_DIR, 'models')

RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw_load_data.csv')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed_data.pkl')
MODEL_PATH = os.path.join(MODEL_DIR, 'lstm_load_model.h5')

SEQ_LENGTH = 24
PREDICTION_HORIZON = 24

TRAIN_SPLIT = 0.8
VALIDATION_SPLIT = 0.1

EPOCHS = 50
BATCH_SIZE = 32
LEARNING_RATE = 0.001

FEATURE_COLS = ['load', 'temperature', 'humidity', 'is_weekend', 'hour']
TARGET_COL = 'load'