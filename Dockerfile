FROM python:3.11-alpine

# system dependencies
RUN apk add --no-cache --virtual .build-deps
RUN apk add libpq

# python dependencies
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN apk del --no-cache .build-deps

# service files
RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src

# run service settings
WORKDIR /src
ENV FLASK_APP=user_profile_matcher/entrypoints/flask_app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1
CMD flask run --host=0.0.0.0 --port=80