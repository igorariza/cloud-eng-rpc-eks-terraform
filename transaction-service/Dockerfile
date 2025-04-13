FROM python:3.9-slim

WORKDIR /app
COPY . /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/*.proto
RUN ls -l /app/

CMD ["python", "client.py"]