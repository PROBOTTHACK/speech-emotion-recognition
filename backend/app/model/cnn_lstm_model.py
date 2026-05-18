import torch
import torch.nn as nn


class CNNLSTMModel(nn.Module):

    def __init__(self, num_classes):

        super(CNNLSTMModel, self).__init__()

        # CNN Feature Extractor
        self.cnn = nn.Sequential(

            # Conv Block 1
            nn.Conv2d(
                in_channels=1,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.BatchNorm2d(32),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Dropout2d(0.2),

            # Conv Block 2
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                padding=1
            ),

            nn.BatchNorm2d(64),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Dropout2d(0.2)

        )

        # LSTM
        self.lstm = nn.LSTM(
            input_size=64 * 32,
            hidden_size=128,
            num_layers=2,
            batch_first=True
        )

        # Final Classifier
        self.fc = nn.Sequential(

            nn.Dropout(0.3),

            nn.Linear(
                128,
                num_classes
            )
        )

    def forward(self, x):

        # CNN Output
        x = self.cnn(x)

        # Shape:
        # (batch, channels, height, width)

        batch_size, channels, height, width = x.size()

        # Reshape for LSTM
        x = x.permute(
            0,
            3,
            1,
            2
        )

        x = x.reshape(
            batch_size,
            width,
            channels * height
        )

        # LSTM
        lstm_output, _ = self.lstm(x)

        # Final Time Step
        x = lstm_output[:, -1, :]

        # Classification
        x = self.fc(x)

        return x