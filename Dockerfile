FROM python:3.11-slim

WORKDIR /app

# --- install system dependencies required for mysqlclient ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# --- copy code into image ---
COPY . /app

# --- install Python dependencies ---
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "MainGame.py"]






