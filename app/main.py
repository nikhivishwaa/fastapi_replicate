from fastapi import FastAPI
from app.routers import image_router

app = FastAPI(
    title="Replicate Image Generator API",
    description="API to fine-tune models and generate images using Replicate",
    version="1.0.0",
)

app.include_router(image_router.router, prefix="/api/v1/images", tags=["Image Generation"])

@app.get('/')
async def welcome():
    return {"message": "Welcome to the Replicate Image Generator API!"}