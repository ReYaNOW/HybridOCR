import asyncio
import hashlib
import io
from typing import List

from PIL import ImageFile, Image
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

# from verbumapi.tesseract_api.recognition import (
#     recognize_text,
#     get_loaded_languages,
# )
from verbumapi.utils import validate_and_read_img, hash_image
from verbumapi.multiproc_manager.manager import (
    tess_img_queue,
    tess_text_shared_dict,
)

# from src.database import get_async_session
# from src.operations.models import Operation
# from src.operations.schemas import OperationCreate, OperationRead

router = APIRouter(
    prefix='/tesseract',
    tags=['Tesseract'],
)


@router.post('/recognize')
def recognize(image: bytes = Depends(validate_and_read_img)):
    pil_image = Image.open(io.BytesIO(image))
    image_hash = hash_image(image)
    
    tess_img_queue.put((pil_image, image_hash))
    
    while image_hash not in tess_text_shared_dict:
        pass

    text, conf = tess_text_shared_dict.pop(image_hash)
    
    # convert conf to a global style
    conf = round(sum(conf) / len(conf) / 100, 3)
    
    return {
        'data': {'text': text, 'confidence': conf},
        'detail': 'text from image was successfully recognized',
    }


# @router.post('/recognize')
# async def recognize(image: bytes = Depends(validate_and_read_img)):
#     pil_image = Image.open(io.BytesIO(image))
#     text = recognize_text(pil_image)
#     return {
#         'data': text,
#         'detail': 'text from image was successfully recognized',
#     }


@router.get('/loaded_languages')
def loaded_languages():
    loaded_langs = get_loaded_languages()
    return {
        'data': loaded_langs,
        'detail': 'languages that were loaded into the model were '
        'successfully received',
    }
