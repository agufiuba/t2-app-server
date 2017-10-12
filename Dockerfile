FROM python:latest

RUN mkdir /as
WORKDIR /as

ADD src /as/src
ADD src /as/src/main
ADD src /as/src/test
ADD requirements.txt /as/requirements.txt

# RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

# RUN apt-get update && apt-get install postgresql-client -y
RUN pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3000
CMD [ "gunicorn", "src.app:app", "-b 0.0.0.0:3000" ]
