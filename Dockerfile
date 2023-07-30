# syntax=docker/dockerfile:1.4

FROM python:3 AS builder
EXPOSE 8000
WORKDIR /ChessApp_v3
COPY requirements.txt /ChessApp_v3
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /ChessApp_v3
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
