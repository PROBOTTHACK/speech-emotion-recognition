import numpy as np


def normalize_features(features):

    mean = np.mean(features)

    std = np.std(features)

    normalized = (
        features - mean
    ) / (std + 1e-8)

    return normalized