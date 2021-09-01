FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /tesseract
WORKDIR /tesseract
ADD requirements.txt /tesseract/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /tesseract/
EXPOSE 80 8000
