import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from torch.utils.data import (
    TensorDataset,
    DataLoader
)

from app.preprocessing.dataset_loader import X, y
from app.model.cnn_lstm_model import CNNLSTMModel

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


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_tensor,
    y_tensor,
    test_size=0.2,
    random_state=42
)


# Dataset + DataLoader
train_dataset = TensorDataset(
    X_train,
    y_train
)

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
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


# Training Loop
epochs = 20

for epoch in range(epochs):

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

    print(
        f"Epoch [{epoch+1}/{epochs}] "
        f"Loss: {running_loss:.4f}"
    )


# Save Model
torch.save(
    model.state_dict(),
    "app/saved_models/cnn_lstm_emotion_model.pth"
)

print("CNN-LSTM Model Saved Successfully")