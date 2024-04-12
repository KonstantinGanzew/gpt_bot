FROM python:3.11-slim-bullseye
WORKDIR /bot
COPY . /bot
RUN /bin/sh -c pip install -r requirements.txt
CMD python app.py