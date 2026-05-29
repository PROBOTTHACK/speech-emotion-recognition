# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.routes.predict_route import router
# from app.model.predict import warm_up_model
# from app.utils.logger import logger

# from app.utils.config import (
#     API_TITLE,
#     API_VERSION
# )


# app = FastAPI(
#     title=API_TITLE,
#     version=API_VERSION
# )


# # CORS
# app.add_middleware(

#     CORSMiddleware,

#     allow_origins=["*"],

#     allow_credentials=True,

#     allow_methods=["*"],

#     allow_headers=["*"],
# )


# app.include_router(router)


# @app.on_event("startup")
# def startup():

#     warm_up_model()
#     logger.info("Model warmup completed")


# @app.get("/")
# def home():

#     return {
#         "message": "Speech Emotion Recognition API Running"
#     }


import asyncio
from contextlib import asynccontextmanager # 1. Import the async context manager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.predict_route import router
from app.model.predict import warm_up_model
from app.utils.logger import logger
from app.utils.config import (
    API_TITLE,
    API_VERSION
)

# 2. Define the background warmup task
async def run_warmup():
    logger.info("Background model warmup initiated...")
    await asyncio.to_thread(warm_up_model)
    logger.info("Model warmup completed successfully in background task")

# 3. Create the modern Lifespan handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This block runs BEFORE the application starts taking requests (Startup)
    asyncio.create_task(run_warmup())
    yield
    # Anything after the 'yield' would run when the app shuts down (Shutdown)

# 4. Pass the lifespan handler into the FastAPI instance
app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    lifespan=lifespan 
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://speech-emotion-recognition-ten.vercel.app",
        "http://localhost:3000",
        "http://localhost:5173"
    ],
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