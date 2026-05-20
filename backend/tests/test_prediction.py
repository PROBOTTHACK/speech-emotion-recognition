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

from app.model.predict import predict_emotion


audio_path = "sample.wav"

prediction = predict_emotion(audio_path)

print("Predicted Emotion:", prediction)