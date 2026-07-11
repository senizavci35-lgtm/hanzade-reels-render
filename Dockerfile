FROM python:3.11-slim

WORKDIR /app

# FFmpeg kurulumu
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyaları
COPY . .

# Cloud Run portu
ENV PORT=8080

CMD ["python", "app.py"]
