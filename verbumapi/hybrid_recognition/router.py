import io
from typing import List

from PIL import ImageFile
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from verbumapi.easyocr_api.recognition import (
    recognize_text,
    get_loaded_languages,
)
from verbumapi.utils import validate_and_read_img

# from src.database import get_async_session
# from src.operations.models import Operation
# from src.operations.schemas import OperationCreate, OperationRead

router = APIRouter(
    prefix='/paddle',
    tags=['PaddleOCR'],
)


@router.post('/recognize')
def recognize(image: io.BytesIO = Depends(validate_and_read_img)):
    text = recognize_text(image)
    return {
        'data': text,
        'detail': 'text from image was successfully recognized',
    }


@router.get('/loaded_languages')
def loaded_languages():
    loaded_langs = get_loaded_languages()
    return {
        'data': loaded_langs,
        'detail': 'languages that were loaded into the model were '
                  'successfully received',
    }
