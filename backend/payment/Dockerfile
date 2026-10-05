FROM python:3.11-slim

WORKDIR /app

COPY payment_service.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003

CMD ["python", "payment_service.py"]