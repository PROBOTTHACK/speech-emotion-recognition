from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

import shutil
import os
from uuid import uuid4

from app.model.predict import predict_emotion

from app.utils.logger import logger

from app.utils.config import TEMP_FOLDER
import traceback
router = APIRouter()


@router.post("/predict")
async def predict_audio(
    file: UploadFile = File(...)
):

    temp_file_path = None
    wav_path = None

    try:

        # Validate file extension
        allowed_extensions = (
            ".wav",
            ".webm"
        )

        filename = file.filename or ""

        if not filename.lower().endswith(allowed_extensions):

            logger.error(
                "Invalid file type uploaded"
            )

            raise HTTPException(
                status_code=400,
                detail="Only .wav and .webm files are supported"
            )

        # Create temp folder
        os.makedirs(
            TEMP_FOLDER,
            exist_ok=True
        )

        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        temp_file_path = os.path.join(
            TEMP_FOLDER,
            f"{uuid4().hex}{file_extension}"
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
        # Convert webm to wav if needed
        if file_extension == ".webm":
            try:
                from pydub import AudioSegment
            except ImportError as exc:
                raise HTTPException(
                    status_code=500,
                    detail=(
                        "WebM conversion requires pydub and FFmpeg. "
                        "Install pydub or upload WAV audio."
                    )
                ) from exc

            wav_path = os.path.join(
                TEMP_FOLDER,
                f"{uuid4().hex}.wav"
            )

            audio = AudioSegment.from_file(
                temp_file_path,
                format="webm"
            )

            audio.export(
                wav_path,
                format="wav"
            )

            prediction = predict_emotion(
                wav_path
            )

            os.remove(wav_path)
            wav_path = None

        else:

            prediction = predict_emotion(
                temp_file_path
            )

        logger.info(
            f"Prediction completed: "
            f"{prediction}"
        )

        # Delete temp file
        os.remove(temp_file_path)
        temp_file_path = None

        return prediction

    except HTTPException:
        raise

    except Exception:

        logger.error(
            traceback.format_exc()
        )

        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )

    finally:
        for path in (wav_path, temp_file_path):
            if path and os.path.exists(path):
                os.remove(path)
