FROM python:3.10-alpine

RUN mkdir "bot"
ADD . /bot

WORKDIR /bot

RUN apt-get update
RUN pip install -r requirements.txt


CMD ["python", "./main.py"]
