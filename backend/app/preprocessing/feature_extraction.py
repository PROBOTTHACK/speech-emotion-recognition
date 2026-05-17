import librosa
import numpy as np


def extract_features(file_path, max_pad_len=128):
    """
    Convert audio file into Mel Spectrogram features
    """

    # STEP 1 — Load audio file
    audio, sample_rate = librosa.load(
        file_path,
        sr=22050
    )

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

    return mel_spectrogram_db