from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    host: str = '0.0.0.0'
    port: int
    secret_key: str

    ocr_module: str = Field(
        description='Name of module to load and then init.'
    )
    languages: list | str = Field(
        description='Languages to load into model.'
        "Example: ['en', 'ru']"
        '(May be different for some models).'
    )

    workers: int = 1

    class Config:
        env_file = '.env'


config = Config()
