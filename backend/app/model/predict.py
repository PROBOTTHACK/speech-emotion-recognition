import torch
import numpy as np

from sklearn.preprocessing import LabelEncoder

from app.model.cnn_lstm_model import CNNLSTMModel
from app.preprocessing.feature_extraction import extract_features
from app.preprocessing.dataset_loader import y


# Device
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# Label Encoder
label_encoder = LabelEncoder()

label_encoder.fit(y)


# Load Model
model = CNNLSTMModel(
    num_classes=len(label_encoder.classes_)
).to(device)

model.load_state_dict(
    torch.load(
        "app/saved_models/best_cnn_lstm_model.pth",
        map_location=device
    )
)

model.eval()


def predict_emotion(audio_path):

    # Extract Features
    features = extract_features(
        audio_path,
        augment=False
    )

    # Convert to tensor
    features_tensor = torch.tensor(
        features,
        dtype=torch.float32
    )

    # Add dimensions
    features_tensor = features_tensor.unsqueeze(0)
    features_tensor = features_tensor.unsqueeze(0)

    features_tensor = features_tensor.to(device)

    # Prediction
    with torch.no_grad():

        outputs = model(features_tensor)

        predicted_index = torch.argmax(
            outputs,
            dim=1
        ).item()

    predicted_emotion = label_encoder.inverse_transform(
        [predicted_index]
    )[0]

    return predicted_emotion