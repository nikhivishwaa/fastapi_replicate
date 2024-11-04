from pydantic import BaseModel, Field
from typing import Optional

class FineTuneRequest(BaseModel):
    model_id: str = Field(..., alias="model_id")  # alias to avoid conflict
    dataset_url: str

    class Config:
        protected_namespaces = ()  # Disable protected namespaces

class GenerateImageRequest(BaseModel):
    model_id: str = Field(..., alias="model_id")
    prompt: str
    image_size: Optional[str] = "1024x1024"

    class Config:
        protected_namespaces = ()  # Disable protected namespaces

class GenerateImageResponse(BaseModel):
    image_url: str

    class Config:
        protected_namespaces = ()  # Disable protected namespaces
