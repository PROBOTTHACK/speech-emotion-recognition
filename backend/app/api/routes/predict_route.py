from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil
import os

from app.model.predict import predict_emotion


router = APIRouter()


@router.post("/predict")
async def predict_audio(
    file: UploadFile = File(...)
):

    # Create temp folder if not exists
    os.makedirs(
        "temp",
        exist_ok=True
    )

    # Temporary file path
    temp_file_path = f"temp/{file.filename}"

    # Save uploaded audio
    with open(temp_file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Predict emotion
    predicted_emotion = predict_emotion(
        temp_file_path
    )

    # Delete temp file
    os.remove(temp_file_path)

    return {
        "predicted_emotion": predicted_emotion
    }