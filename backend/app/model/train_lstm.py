import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

from torch.utils.data import (
    TensorDataset,
    DataLoader
)

from app.preprocessing.dataset_loader import X, y
from app.model.cnn_lstm_model import CNNLSTMModel


# Device
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Using Device:", device)


# Encode labels
label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)


# Convert to tensors
X_tensor = torch.tensor(
    X,
    dtype=torch.float32
)

# Add channel dimension
X_tensor = X_tensor.unsqueeze(1)

y_tensor = torch.tensor(
    y_encoded,
    dtype=torch.long
)


# Train / Validation Split
X_train, X_val, y_train, y_val = train_test_split(
    X_tensor,
    y_tensor,
    test_size=0.2,
    random_state=42
)


# Dataset
train_dataset = TensorDataset(
    X_train,
    y_train
)

val_dataset = TensorDataset(
    X_val,
    y_val
)


# DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=32,
    shuffle=False
)


# Model
model = CNNLSTMModel(
    num_classes=len(label_encoder.classes_)
).to(device)


# Loss Function
criterion = nn.CrossEntropyLoss()


# Optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# Training
epochs = 20

for epoch in range(epochs):

    # TRAINING MODE
    model.train()

    running_loss = 0.0

    for batch_X, batch_y in train_loader:

        batch_X = batch_X.to(device)
        batch_y = batch_y.to(device)

        optimizer.zero_grad()

        outputs = model(batch_X)

        loss = criterion(
            outputs,
            batch_y
        )

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    train_loss = running_loss / len(train_loader)

    # VALIDATION MODE
    model.eval()

    val_loss = 0.0

    all_predictions = []
    all_labels = []

    with torch.no_grad():

        for val_X, val_y in val_loader:

            val_X = val_X.to(device)
            val_y = val_y.to(device)

            outputs = model(val_X)

            loss = criterion(
                outputs,
                val_y
            )

            val_loss += loss.item()

            predictions = torch.argmax(
                outputs,
                dim=1
            )

            all_predictions.extend(
                predictions.cpu().numpy()
            )

            all_labels.extend(
                val_y.cpu().numpy()
            )

    val_loss /= len(val_loader)

    val_accuracy = accuracy_score(
        all_labels,
        all_predictions
    )

    print(
        f"Epoch [{epoch+1}/{epochs}] | "
        f"Train Loss: {train_loss:.4f} | "
        f"Val Loss: {val_loss:.4f} | "
        f"Val Accuracy: {val_accuracy * 100:.2f}%"
    )


# Save Model
torch.save(
    model.state_dict(),
    "app/saved_models/cnn_lstm_emotion_model.pth"
)

print("CNN-LSTM Model Saved Successfully")