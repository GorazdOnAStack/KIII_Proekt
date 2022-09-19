# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DockerHOME=.  
WORKDIR $DockerHOME  
COPY . $DockerHOME
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver
