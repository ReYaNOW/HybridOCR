from verbumapi.tesseract_api.recognition import recognize_text as tess_recog
from


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
