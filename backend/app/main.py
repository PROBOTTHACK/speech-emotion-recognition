from fastapi import FastAPI

from app.api.routes.predict_route import router


app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Speech Emotion Recognition API Running"
    }

app.include_router(router)