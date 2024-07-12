def tesserocr_init(languages: str):
    import tesserocr
    import os

    TESSDATA_PREFIX = os.getenv('TESSDATA_PREFIX')
    model = tesserocr.PyTessBaseAPI(
        path=TESSDATA_PREFIX,  # noqa Getting unexpected args by PyCharm
        lang=languages,  # noqa
    )
    model.SetVariable('debug_file', '/dev/null')
    return model


def easyocr_init(languages: str):
    import easyocr

    # verbose=False means there will not going to be message
    # 'Using CPU. Note: This module is much faster with a GPU.'
    model = easyocr.Reader(languages.split(','), gpu=False, verbose=False)
    return model
