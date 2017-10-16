FROM python:latest

RUN mkdir /as
WORKDIR /as

ADD src /as/src
ADD src /as/src/main
ADD src /as/src/test
ADD requirements.txt /as/requirements.txt
ADD serviceAccountKey.json /as/src/main/firebase/serviceAccountKey.json

RUN pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3000
CMD [ "gunicorn", "src.app:app", "-b 0.0.0.0:3000" ]
