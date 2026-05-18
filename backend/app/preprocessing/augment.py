import numpy as np
import librosa


def add_noise(audio, noise_factor=0.005):

    noise = np.random.randn(len(audio))

    augmented_audio = audio + noise_factor * noise

    return augmented_audio


def pitch_shift(audio, sample_rate, n_steps=2):

    return librosa.effects.pitch_shift(
        audio,
        sr=sample_rate,
        n_steps=n_steps
    )


def time_stretch(audio, rate=0.8):

    return librosa.effects.time_stretch(
        audio,
        rate=rate
    )