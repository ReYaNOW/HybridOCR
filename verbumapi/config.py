import os

from dotenv import load_dotenv

load_dotenv()

TESSDATA_PREFIX = os.getenv('TESSDATA_PREFIX')
