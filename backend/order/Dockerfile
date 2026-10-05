FROM python:3.11-slim

WORKDIR /app

COPY order_service.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "order_service.py"]