FROM python:3.9-slim

WORKDIR /app

COPY . /app
COPY requirements.txt /app/requirements.txt
COPY ../proto /app/proto

RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/*.proto


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]