
# pull official base image

FROM python:3.10-slim

RUN apt-get update

RUN apt-get install libpq-dev -y
RUN apt-get install python3-dev build-essential -y
RUN apt-get install postgresql-client -y

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV




ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /srv/app
WORKDIR /srv/app


# pip install -r requirements.txt



# python manage.py runserver

# python manage.py migrate