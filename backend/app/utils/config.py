import torch


# Device
DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# Audio
SAMPLE_RATE = 22050
MAX_PAD_LEN = 128


# Model
MODEL_PATH = (
    "app/saved_models/best_cnn_lstm_model.pth"
)


# Uploads
TEMP_FOLDER = "temp"


# API
API_TITLE = "Speech Emotion Recognition API"
API_VERSION = "1.0.0"