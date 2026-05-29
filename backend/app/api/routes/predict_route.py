from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

import shutil
import os
import time
from uuid import uuid4

from app.model.predict import predict_emotion

from app.utils.logger import logger

from app.utils.config import TEMP_FOLDER
import traceback
router = APIRouter()
MAX_UPLOAD_SIZE = 10 * 1024 * 1024


@router.post("/predict")
async def predict_audio(
    file: UploadFile = File(...)
):

    temp_file_path = None
    wav_path = None
    started_at = time.perf_counter()

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

        file_size = os.path.getsize(temp_file_path)

        if file_size > MAX_UPLOAD_SIZE:
            raise HTTPException(
                status_code=413,
                detail="Audio file is too large. Record a shorter clip."
            )

        logger.info(
            f"File uploaded: {file.filename} ({file_size} bytes)"
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
            f"{prediction} in {time.perf_counter() - started_at:.2f}s"
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
