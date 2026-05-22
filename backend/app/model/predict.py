import torch
import numpy as np

from sklearn.preprocessing import LabelEncoder

from app.model.cnn_lstm_model import CNNLSTMModel
from app.preprocessing.feature_extraction import extract_features
from app.preprocessing.dataset_loader import y
import torch.nn.functional as F

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

        # Softmax probabilities
        probabilities = F.softmax(
            outputs,
            dim=1
        )

        # Predicted class
        confidence, predicted_index = torch.max(
            probabilities,
            dim=1
        )

        predicted_index = predicted_index.item()

        confidence = confidence.item()

        # Convert all probabilities
        probabilities_list = (
            probabilities.squeeze()
            .cpu()
            .numpy()
        )

    # Emotion label
    predicted_emotion = label_encoder.inverse_transform(
        [predicted_index]
    )[0]

    # Build probability dictionary
    probability_dict = {}

    for emotion, probability in zip(
        label_encoder.classes_,
        probabilities_list
    ):

        probability_dict[emotion] = round(
            float(probability * 100),
            2
        )

    return {

        "emotion": predicted_emotion,

        "confidence": round(
            confidence * 100,
            2
        ),

        "probabilities": probability_dict
    }