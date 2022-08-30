FROM python:3.6.8

WORKDIR /test-project

COPY requirements.txt .

RUN pip install -r requirements.txt

VOLUME [/test-project]

EXPOSE 5000

ENV HOST 0.0.0.0

CMD [ "python","app.py"]

