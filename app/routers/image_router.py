from fastapi import APIRouter, HTTPException
import requests
from app.schemas.image import FineTuneRequest, GenerateImageRequest, GenerateImageResponse
from app.services import replicate_service 

router = APIRouter()

@router.post("/fine-tune")
async def fine_tune(request: FineTuneRequest):
    try:
        result = replicate_service.fine_tune_model(request.model_id, request.dataset_url)
        return {"message": "Model fine-tuning started", "details": result}
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@router.post("/generate", response_model=GenerateImageResponse)
async def generate(request: GenerateImageRequest):
    try:
        result = replicate_service.generate_image(request.model_id, request.prompt, request.image_size)
        return GenerateImageResponse(image_url=result["output"]["url"])
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
