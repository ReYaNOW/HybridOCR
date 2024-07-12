ARG OCR_NAME

FROM python:3.12-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install fastapi pydantic pydantic_settings


FROM base AS tesseract
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && pip install tesserocr pillow
# Using separate RUN cuz this line may change more often
RUN apt-get install tesseract-ocr-rus
ENV TESSDATA_PREFIX="/usr/share/tesseract-ocr/5/tessdata/"


FROM base AS easyocr
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install easyocr


FROM base AS paddleocr
RUN apt-get update \
    && apt-get -y install libglib2.0-0 libgomp1 libgl1 \
    && pip install paddlepaddle paddleocr requests



FROM ${OCR_NAME} AS final

WORKDIR /usr/local/src/${OCR_NAME}

COPY ./.env .
COPY ocr_microservice ./ocr_microservice

CMD ["python3", "ocr_microservice/main.py"]
