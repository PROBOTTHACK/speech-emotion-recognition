import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app.preprocessing.feature_extraction import extract_features
import matplotlib.pyplot as plt


audio_path = "datasets/ravdess/Actor_01/03-01-05-01-01-01-01.wav"

features = extract_features(audio_path)

print("Feature Shape:", features.shape)

plt.figure(figsize=(10, 4))

plt.imshow(
    features,
    origin='lower',
    aspect='auto'
)

plt.colorbar()

plt.title("Mel Spectrogram")

plt.xlabel("Time")
plt.ylabel("Frequency")

plt.show()