FROM python:3.11-slim

WORKDIR /app

COPY product_service.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "product_service.py"]