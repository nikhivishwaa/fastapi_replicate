import requests
from app.config import settings

def fine_tune_model(model_id: str, dataset_url: str):
    url = f"{settings.REPLICATE_API_URL}/{model_id}/fine-tune"
    headers = {"Authorization": f"Token {settings.REPLICATE_API_TOKEN}"}
    payload = {"dataset_url": dataset_url}
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def generate_image(model_id: str, prompt: str, image_size: str):
    url = f"{settings.REPLICATE_API_URL}/{model_id}/generate"
    headers = {"Authorization": f"Token {settings.REPLICATE_API_TOKEN}"}
    payload = {"prompt": prompt, "image_size": image_size}
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
