"""Create fastapi rest api to fetch model"""

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    """Sample api"""
    return {"message": "Hello World"}


@app.get("/model_download")
async def model():
    """Fetch model api"""
    return FileResponse(
        "churn-modelling-kedro/predictor.pkl",
        filename="predictor.pkl",
        media_type="application/octet-stream"
    )
