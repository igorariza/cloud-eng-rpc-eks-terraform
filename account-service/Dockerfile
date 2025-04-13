FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./app/proto/*.proto


CMD ["python", "server.py"]