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
from app.model.cnn_model import CNNModel


# Encode string labels → numbers
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


# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_tensor,
    y_tensor,
    test_size=0.2,
    random_state=42
)


# DataLoader
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
model = CNNModel(
    num_classes=len(label_encoder.classes_)
)


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

        # Clear gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(batch_X)

        # Compute loss
        loss = criterion(
            outputs,
            batch_y
        )

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch [{epoch+1}/{epochs}] "
        f"Loss: {running_loss:.4f}"
    )


# Save model
torch.save(
    model.state_dict(),
    "app/saved_models/cnn_emotion_model.pth"
)

print("Model Saved Successfully")