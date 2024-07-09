import hashlib

from fastapi import UploadFile, HTTPException


async def validate_and_read_img(image: UploadFile):
    if not image.content_type.startswith('image/'):
        raise HTTPException(
            status_code=415,
            detail={
                'data': None,
                'detail': 'Only images are allowed',
            },
        )

    return await image.read()


def hash_image(image: bytes):
    return hashlib.md5(image).hexdigest()
