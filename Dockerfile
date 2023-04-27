# Dockerfile
FROM python:3.9-slim

WORKDIR /iot_pot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY iot_server.py iot_client.py iot_runner.py ./

EXPOSE 5683/udp
EXPOSE 5684/udp

CMD ["python", "iot_runner.py"]
