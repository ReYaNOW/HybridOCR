import io

from PIL import Image


def tesserocr_recognize_text(model, image: bytes) -> tuple[str, float]:
    image = Image.open(io.BytesIO(image))

    model.SetImage(image)
    text = model.GetUTF8Text()
    conf = model.AllWordConfidences()
    conf = sum(conf) / len(conf) / 100
    return text, conf


def easyocr_recognize_text(model, image: bytes) -> tuple[str, float]:
    result = model.readtext(
        image,
        decoder='wordbeamsearch',
        beamWidth=15,
    )
    _, text, conf = result[0]
    return text, conf
