import multiprocessing

from fastapi import FastAPI

from verbumapi.easyocr_api.router import router as router_easyocr
from verbumapi.tesseract_api.router import router as router_pytesseract
# from verbumapi.paddle_api.router import router as router_paddle

from verbumapi.multiproc_manager.manager import (
    tess_img_queue,
    tess_text_shared_dict,
    easyocr_img_queue,
    easyocr_text_shared_dict
)
from verbumapi.tesseract_api.recognition import tess_process
from verbumapi.easyocr_api.recognition import easyocr_process


app = FastAPI(title='VerbumAPI')


app.include_router(router_pytesseract)
app.include_router(router_easyocr)
# app.include_router(router_paddle)

tess_process = multiprocessing.Process(
    target=tess_process, args=(tess_img_queue, tess_text_shared_dict)
)

tess_process.start()

easyocr_process = multiprocessing.Process(
    target=easyocr_process, args=(easyocr_img_queue, easyocr_text_shared_dict)
)

easyocr_process.start()
