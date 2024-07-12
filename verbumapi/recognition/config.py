from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    tesserocr_addr: HttpUrl = 'http://127.0.0.1:8081'
    easyocr_addr: HttpUrl = 'http://127.0.0.1:8082'
    secret_key: str
    
    class Config:
        env_file = '.env'


config = Config()

ocr_model_addresses = {
    'tesserocr': config.tesserocr_addr,
    'easyocr': config.easyocr_addr,
}
