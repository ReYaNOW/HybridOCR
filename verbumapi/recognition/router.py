from fastapi import APIRouter, Depends

from verbumapi.recognition.config import ocr_model_addresses
from verbumapi.recognition.dependencies import (
    check_model_exist,
    httpx_client,
    validate_img,
)
from verbumapi.recognition.schemas import (
    LanguagesResponse,
    RecognizeResponse,
)
from verbumapi.recognition.service import (
    request_image_api,
    request_languages_api,
)

router = APIRouter(
    prefix='/recognition',
    tags=['Recognition'],
)


@router.get('')
async def get_list_of_models() -> dict:
    return ocr_model_addresses


@router.post('{model}/recognize', response_model=RecognizeResponse)
async def recognize(
    model=Depends(check_model_exist),
    client=Depends(httpx_client),
    image=Depends(validate_img),
):
    data = await request_image_api(client, model, image)
    return RecognizeResponse(data=data.json())


@router.get('{model}/languages', response_model=LanguagesResponse)
async def loaded_languages(
    model=Depends(check_model_exist), client=Depends(httpx_client)
):
    langs_data = await request_languages_api(client, model)
    return LanguagesResponse(languages=langs_data.json())
