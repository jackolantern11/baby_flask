FROM python:3.9-alpine

ENV FLASK_APP main.py
ENV FLASK_CONFIG production

# numpy & pandas dependencies reqd
RUN apk add --no-cache --update \
    python3 python3-dev gcc g++ \
    gfortran musl-dev \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN adduser -D baby_flask
USER baby_flask

WORKDIR /home/baby_flask

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY data data
COPY main.py config.py boot.sh data-dev.sqlite ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
