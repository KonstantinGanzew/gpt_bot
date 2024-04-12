FROM python:3.8.19-alpine3.19
WORKDIR /bot
COPY . /bot
RUN pip install requests==2.31.0 &&\
    pip install python-dotenv==1.0.1 &&\
    pip install openai==1.14.3 &&\
    pip install aiogram==2.9
RUN /bin/sh -c pip install logging==0.4.9.6
CMD python app.py