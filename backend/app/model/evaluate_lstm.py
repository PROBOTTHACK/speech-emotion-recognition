import torch
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from app.preprocessing.dataset_loader import X, y
from app.model.cnn_lstm_model import CNNLSTMModel


# Encode Labels
label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)


# Convert to tensors
X_tensor = torch.tensor(
    X,
    dtype=torch.float32
)

X_tensor = X_tensor.unsqueeze(1)

y_tensor = torch.tensor(
    y_encoded,
    dtype=torch.long
)


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_tensor,
    y_tensor,
    test_size=0.2,
    random_state=42
)


# Device
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Using Device:", device)


# Load Model
model = CNNLSTMModel(
    num_classes=len(label_encoder.classes_)
).to(device)

model.load_state_dict(
    torch.load(
        "app/saved_models/cnn_lstm_emotion_model.pth",
        map_location=device
    )
)

model.eval()


# Move test data to GPU
X_test = X_test.to(device)


# Prediction
with torch.no_grad():

    outputs = model(X_test)

    predictions = torch.argmax(
        outputs,
        dim=1
    )


# Move back to CPU
predictions = predictions.cpu()


# Accuracy
accuracy = accuracy_score(
    y_test.numpy(),
    predictions.numpy()
)

print(f"Accuracy: {accuracy * 100:.2f}%")


# Confusion Matrix
cm = confusion_matrix(
    y_test.numpy(),
    predictions.numpy()
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=label_encoder.classes_
)

display.plot(cmap="Blues")

plt.title("CNN-LSTM Confusion Matrix")

plt.show()