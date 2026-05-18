import librosa
import numpy as np
from app.preprocessing.normalize import normalize_features
import random

from app.preprocessing.augment import (
    add_noise,
    pitch_shift,
    time_stretch
)
def extract_features(file_path,augment=False, max_pad_len=128):
    """
    Convert audio file into Mel Spectrogram features
    """
    

    # STEP 1 — Load audio file
    audio, sample_rate = librosa.load(
        file_path,
        sr=22050
    )
    # Random Augmentation
    if augment:

        augmentation_choice = random.choice([
            "noise",
            "pitch",
            "stretch",
            "none"
        ])

        if augmentation_choice == "noise":

            audio = add_noise(audio)

        elif augmentation_choice == "pitch":

            audio = pitch_shift(
                audio,
                sample_rate
            )

        elif augmentation_choice == "stretch":

            audio = time_stretch(audio)

    # STEP 2 — Generate Mel Spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate,
        n_mels=128
    )

    # STEP 3 — Convert to Decibel Scale
    mel_spectrogram_db = librosa.power_to_db(
        mel_spectrogram,
        ref=np.max
    )

    # STEP 4 — Padding / Truncating
    if mel_spectrogram_db.shape[1] < max_pad_len:

        pad_width = max_pad_len - mel_spectrogram_db.shape[1]

        mel_spectrogram_db = np.pad(
            mel_spectrogram_db,
            pad_width=((0, 0), (0, pad_width)),
            mode='constant'
        )

    else:
        mel_spectrogram_db = mel_spectrogram_db[:, :max_pad_len]

    normalized_features = normalize_features(
        mel_spectrogram_db
    )

    return normalized_features