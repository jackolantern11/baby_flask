FROM python:3.9

ENV FLASK_APP main.py
ENV FLASK_CONFIG production

# numpy & pandas dependencies reqd
RUN apt-get update --fix-missing \
    && apt-get install -yqq \
        default-jre-headless \
        gcc \
        build-essential \
        ldap-utils \
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        libaio1 \
        libpq-dev \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && ldconfig

RUN addgroup --gid "50000" "baby_flask" && \
    adduser --quiet "baby_flask" --uid "50000" \
    --gid "50000"

USER baby_flask

WORKDIR /home/baby_flask

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements/common.txt

COPY app app
# COPY data data
COPY main.py config.py boot.sh data-dev.sqlite ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
