FROM python:3-alpine3.15
WORKDIR /app
COPY . /app

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip

ADD requirements.txt .

RUN pip install -r requirements.txt
CMD python ./app.py