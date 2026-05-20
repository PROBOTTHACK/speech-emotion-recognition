from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.predict_route import router

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


@app.get("/")
def home():

    return {
        "message": "Speech Emotion Recognition API Running"
    }