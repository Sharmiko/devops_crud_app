FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir /app/devops_crud_app
WORKDIR /app

RUN apt-get update -y

ADD requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD devops_crud_app /app/devops_crud_app

WORKDIR /app/devops_crud_app/
