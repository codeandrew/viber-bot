FROM python:3.7.1-alpine3.7

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
