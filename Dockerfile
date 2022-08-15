FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django-bert
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
