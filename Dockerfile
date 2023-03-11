ARG API_ID
ARG API_HASH

FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py ./

VOLUME /app
ENTRYPOINT [ "python", "/app/main.py" ]

LABEL org.opencontainers.image.source=https://github.com/kozalosev/tg-wipe
LABEL org.opencontainers.image.description="A simple Python script to wipe a user's messages out from some chat"
LABEL org.opencontainers.image.licenses=MIT
