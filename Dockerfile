FROM python:3.9-alpine3.14
ADD . /code
WORKDIR /code
RUN pip instal -r requirements.txt
CMD ["python", "api.py"]

