import torch
import torch.nn as nn


class CNNModel(nn.Module):

    def __init__(self, num_classes):

        super(CNNModel, self).__init__()

        self.cnn = nn.Sequential(

            # Conv Block 1
            nn.Conv2d(
                in_channels=1,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(
                kernel_size=2
            ),

            # Conv Block 2
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(
                kernel_size=2
            )

        )

        # Fully Connected Layer
        self.fc = nn.Sequential(

            nn.Flatten(),

            nn.Linear(
                64 * 32 * 32,
                128
            ),

            nn.ReLU(),

            nn.Dropout(0.3),

            nn.Linear(
                128,
                num_classes
            )
        )

    def forward(self, x):

        x = self.cnn(x)

        x = self.fc(x)

        return x