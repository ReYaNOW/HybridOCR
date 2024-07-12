import httpx
from fastapi import UploadFile, HTTPException

from verbumapi.recognition.config import ocr_model_addresses


async def check_model_exist(model: str):
    if model not in ocr_model_addresses:
        raise HTTPException(
            status_code=404, detail='OCR Model with such name is not found'
        )
    return model


async def validate_img(image: UploadFile):
    if not image.content_type.startswith('image/'):
        raise HTTPException(
            status_code=415,
            detail='Only images are allowed',
        )
    return image


async def httpx_client() -> httpx.AsyncClient:
    async with httpx.AsyncClient() as client:
        yield client
