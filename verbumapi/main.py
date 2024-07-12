from fastapi import FastAPI

from verbumapi.recognition.router import router as recognition_router

app = FastAPI(title='VerbumAPI')

app.include_router(recognition_router)
