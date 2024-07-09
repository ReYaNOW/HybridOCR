from multiprocessing.queues import Queue
from multiprocessing.managers import DictProxy # noqa

# import tesserocr
from fastapi import File

from verbumapi.config import TESSDATA_PREFIX

# if TESSDATA_PREFIX:
#     model = tesserocr.PyTessBaseAPI(
#         path=TESSDATA_PREFIX, lang='eng+rus'
#     )  # noqa
# else:
#     model = tesserocr.PyTessBaseAPI()
#
# model.SetVariable('debug_file', '/dev/null')


def tess_process(img_queue: Queue, text_shared_dict: DictProxy):
    # Импорт и инициализация моделей внутри процесса
    import tesserocr
    model = tesserocr.PyTessBaseAPI(
        path=TESSDATA_PREFIX, lang='eng+rus'  # noqa
    )
    model.SetVariable('debug_file', '/dev/null')

    # Ожидание новых изображений и их обработка
    while True:
        if img_queue.empty():
            continue
        image, img_hash = img_queue.get(
        )  # Получаем изображение из очереди
        # Обработка изображения

        model.SetImage(image)
        text = model.GetUTF8Text()
        conf = model.AllWordConfidences()
        
        # Помещаем результат в очередь для ответа
        text_shared_dict[img_hash] = (text, conf)


# def recognize_text(image: File):
#     model.SetImage(image)
#     return model.GetUTF8Text()
#
#
# def get_loaded_languages():
#     return model.GetLoadedLanguages()
