# src/main.py
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "app": "flux-demo",
        "version": os.getenv("APP_VERSION", "dev")
    }

@app.get("/health")
def health():
    return {"status": "ok"}
