import io

from paddleocr import PaddleOCR

list_of_langs = ['en', 'ru']
model = PaddleOCR(use_angle_cls=True, lang=list_of_langs)


def recognize_text(image: io.BytesIO):
    result = model.ocr(image, cls=True, det=False)
    
    text, conf = None, None
    for i in range(len(result)):
        res = result[i]
        for line in res:
            text, conf = line
    return text


def get_loaded_languages():
    return list_of_langs
