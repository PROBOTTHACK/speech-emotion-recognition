import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import torch

from app.model.cnn_lstm_model import CNNLSTMModel


model = CNNLSTMModel(
    num_classes=7
)

dummy_input = torch.randn(
    32,
    1,
    128,
    128
)

output = model(dummy_input)

print("Output Shape:", output.shape)