from multiprocessing import Manager


manager = Manager()

tess_img_queue = manager.Queue()
tess_text_shared_dict = manager.dict()

easyocr_img_queue = manager.Queue()
easyocr_text_shared_dict = manager.dict()
