from pydantic import BaseModel, NonNegativeFloat


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
