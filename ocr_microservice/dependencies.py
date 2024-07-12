from fastapi import UploadFile


async def async_read_img(image: UploadFile):
    return await image.read()
