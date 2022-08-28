FROM python:3.8.10

ARG SERVER
ARG PORT
ARG DOMAIN
ARG CERT_COUNTRY_NAME
ARG CERT_STATE
ARG CERT_LOCATION
ARG CERT_ORG_NAME
ARG CERT_ORG_UNIT_NAME
ARG CERT_COMMON_NAME
ARG CERT_EMAIL

ENV PYTHONUNBUFFERED=1

EXPOSE ${PORT}

RUN mkdir /bot_backend
WORKDIR /bot_backend

RUN addgroup --system bot_user && adduser --system --group bot_user; \
    if [ "$SERVER" = "production" ]; then \
        openssl req -newkey rsa:2048 -sha256 -nodes -keyout 'private.key' -x509 -days 3650 -out \
        'cert.pem' -subj "/C=${CERT_COUNTRY_NAME}/ST=${CERT_STATE}/L=${CERT_LOCATION}/O=${CERT_ORG_NAME}/OU=${CERT_ORG_UNIT_NAME}/CN=${CERT_COMMON_NAME}/emailAddress=${CERT_EMAIL}"; \
        chown bot_user ./cert.pem; \
        chown bot_user ./private.key; \
    fi

USER bot_user

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt;

COPY . .