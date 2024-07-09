import asyncio
import hashlib
import io
from typing import List

from PIL import ImageFile
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from verbumapi.easyocr_api.recognition import get_loaded_languages
from verbumapi.multiproc_manager.manager import (
    easyocr_img_queue,
    easyocr_text_shared_dict,
)

# from verbumapi.easyocr_api.recognition import (
#     recognize_text,
#     get_loaded_languages,
# )
from verbumapi.utils import validate_and_read_img, hash_image

# from src.database import get_async_session
# from src.operations.models import Operation
# from src.operations.schemas import OperationCreate, OperationRead

router = APIRouter(
    prefix='/easyocr',
    tags=['EasyOCR'],
)


@router.post('/recognize')
def recognize(image: bytes = Depends(validate_and_read_img)):
    image_hash = hashlib.md5(image).hexdigest()

    easyocr_img_queue.put((image, image_hash))

    while image_hash not in easyocr_text_shared_dict:
        pass

    text, conf = easyocr_text_shared_dict.pop(image_hash)
    return {
        'data': {'text': text, 'confidence': conf},
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
