FROM python:latest

RUN mkdir /as
WORKDIR /as

RUN pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org flask gunicorn

ADD src /as/src

EXPOSE 3000
CMD [ "gunicorn", "src.main:app", "-b 0.0.0.0:3000" ]
