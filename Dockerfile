FROM python:3.8.10
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN mkdir /code
WORKDIR /code
