import httpx

from verbumapi.recognition.config import config, ocr_model_addresses


async def request_image_api(client: httpx.AsyncClient, model, image):
    url = f'{ocr_model_addresses[model]}{model}/recognize'
    return await client.post(
        url,
        data={'secret_key': config.secret_key},
        files={'image': image.file},
    )


async def request_languages_api(client: httpx.AsyncClient, model):
    url = f'{ocr_model_addresses[model]}{model}/languages'
    return await client.get(url)
