from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.predict_route import router
from app.model.predict import warm_up_model
from app.utils.logger import logger

from app.utils.config import (
    API_TITLE,
    API_VERSION
)


app = FastAPI(
    title=API_TITLE,
    version=API_VERSION
)


# CORS
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(router)


@app.on_event("startup")
def startup():

    warm_up_model()
    logger.info("Model warmup completed")


@app.get("/")
def home():

    return {
        "message": "Speech Emotion Recognition API Running"
    }
