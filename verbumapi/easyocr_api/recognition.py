from multiprocessing.managers import DictProxy  # noqa
from multiprocessing.queues import Queue

list_of_langs = ['en', 'ru']


def easyocr_process(img_queue: Queue, text_shared_dict: DictProxy):
    # Импорт и инициализация моделей внутри процесса
    import easyocr

    model = easyocr.Reader(list_of_langs)

    # Ожидание новых изображений и их обработка
    while True:
        if img_queue.empty():
            continue
        image, img_hash = img_queue.get()  # Получаем изображение из очереди
        # Обработка изображения

        result = model.readtext(
            image,
            # paragraph=True,
            # detail=0,
            decoder='wordbeamsearch',
            beamWidth=15,
        )
        _, text, conf = result[0]

        # Помещаем результат в очередь для ответа
        text_shared_dict[img_hash] = (text, conf)


def get_loaded_languages():
    return list_of_langs
