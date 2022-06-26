FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/

RUN python3 manage.py makemigrations