FROM python:3.6.8

WORKDIR /test-project

COPY * .

RUN pip install -r requirements.txt

VOLUME ["/test-project"]

EXPOSE 5000

ENV DEBUG true

ENV CELERY_BROKER_URL redis://localhost:6379/0

ENV CELERY_RESULT_BACKEND redis://localhost:6379/0

ENV HOST 0.0.0.0

CMD ["gunicorn","--bind","0.0.0.0:5000","app:app","--preload"]