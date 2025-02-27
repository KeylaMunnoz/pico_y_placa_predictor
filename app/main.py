from fastapi import FastAPI
from app.routes import predictor

app = FastAPI(title="Pico y Placa Predictor API")

app.include_router(predictor.router)