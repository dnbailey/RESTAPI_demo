FROM python:3.10

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD ./src .

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "main:app" ]
