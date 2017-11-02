FROM python:latest

RUN mkdir /as
WORKDIR /as

COPY requirements.txt /as/requirements.txt

RUN pip install -r requirements.txt

COPY src /as/src

EXPOSE 3000

CMD [ "gunicorn", "--chdir", "src", "app:app", "-b 0.0.0.0:3000" ]
