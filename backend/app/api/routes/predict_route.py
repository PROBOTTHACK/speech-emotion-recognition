from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

import shutil
import os

from app.model.predict import predict_emotion

from app.utils.logger import logger

from app.utils.config import TEMP_FOLDER


router = APIRouter()


@router.post("/predict")
async def predict_audio(
    file: UploadFile = File(...)
):

    try:

        # Validate file extension
        if not file.filename.endswith(".wav"):

            logger.error(
                "Invalid file type uploaded"
            )

            raise HTTPException(
                status_code=400,
                detail="Only .wav files are supported"
            )

        # Create temp folder
        os.makedirs(
            TEMP_FOLDER,
            exist_ok=True
        )

        temp_file_path = (
            f"{TEMP_FOLDER}/{file.filename}"
        )

        # Save uploaded file
        with open(
            temp_file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        logger.info(
            f"File uploaded: {file.filename}"
        )

        # Prediction
        prediction = predict_emotion(
            temp_file_path
        )

        logger.info(
            f"Prediction completed: "
            f"{prediction}"
        )

        # Delete temp file
        os.remove(temp_file_path)

        return prediction

    except Exception as e:

        logger.error(
            f"Prediction Error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )