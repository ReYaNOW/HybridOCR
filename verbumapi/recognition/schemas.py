import httpx
from fastapi import UploadFile
from pydantic import BaseModel, HttpUrl, NonNegativeFloat, TypeAdapter

from verbumapi.recognition.config import config


class RecognizeDetails(BaseModel):
    text: str
    conf: NonNegativeFloat


class RecognizeResponse(BaseModel):
    data: RecognizeDetails
    detail: str = 'Text from image was successfully recognized'


class LanguagesResponse(BaseModel):
    languages: str
    detail: str = (
        'Languages that were loaded into the model were '
        'successfully received'
    )


class OCRApiRequest(BaseModel):
    image: UploadFile | None = None
    ocr_module: str
    address: HttpUrl


class TesserOCRRequest(OCRApiRequest):
    address: HttpUrl = config.tesserocr_addr
    ocr_module: str = 'tesserocr'
