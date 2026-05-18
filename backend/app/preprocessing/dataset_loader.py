import os
import numpy as np

from app.preprocessing.feature_extraction import extract_features
from app.utils.labels import emotion_map


DATASET_PATH = "datasets/ravdess"


X = []
y = []


# Traverse actor folders
for actor_folder in os.listdir(DATASET_PATH):

    actor_path = os.path.join(
        DATASET_PATH,
        actor_folder
    )

    # Skip non-folder files
    if not os.path.isdir(actor_path):
        continue

    # Traverse audio files
    for audio_file in os.listdir(actor_path):

        file_path = os.path.join(
            actor_path,
            audio_file
        )

        # Extract emotion code
        parts = audio_file.split("-")

        # Skip invalid files
        if len(parts) < 3:
            continue

        emotion_code = parts[2]

        # Ignore unsupported labels
        if emotion_code not in emotion_map:
            continue

        # Extract Mel Spectrogram
        features = extract_features(file_path)

        # Store data
        X.append(features)
        y.append(emotion_map[emotion_code])


# Convert to numpy arrays
X = np.array(X)
y = np.array(y)


print("Dataset Loaded Successfully")

print("Feature Shape:", X.shape)
print("Labels Shape:", y.shape)

print("Unique Labels:")
print(np.unique(y))