import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Body

import initializers
import recognition
from dependencies import async_read_img
from micro_config import config

initialize_model = getattr(initializers, f'{config.ocr_module}_init')
model = initialize_model(config.languages)

recognize_text = getattr(recognition, f'{config.ocr_module}_recognize_text')

app = FastAPI(title=f'{config.ocr_module.capitalize()}API')


@app.post(f'/{config.ocr_module}/recognize')
def recognize(
    secret_key: str = Body(...), image: bytes = Depends(async_read_img)
):
    if not config.secret_key == secret_key:
        raise HTTPException(status_code=401, detail='Incorrect secret key')

    text, conf = recognize_text(model, image)
    return {'text': text, 'conf': conf}


@app.get(f'/{config.ocr_module}/languages')
async def loaded_languages():
    return config.languages


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host=config.host, port=config.port, workers=config.workers
    )
