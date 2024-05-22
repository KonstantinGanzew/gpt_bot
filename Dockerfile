FROM python:3.8.19-alpine3.19

WORKDIR /bot
COPY . /bot

RUN pip install requests==2.31.0 \
    python-dotenv==1.0.1 \
    openai==1.14.3 \
    aiogram==2.9 &&\
    /bin/sh -c pip install logging==0.4.9.6 &&\
    mkdir -p /bot/bd/base &&\
    touch /bot/bd/base/db.sql

CMD ["python", "app.py"]