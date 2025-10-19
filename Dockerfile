FROM python:3.11-slim

# Set working directory
WORKDIR /app

# ---- Install system dependencies for mysqlclient ----
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy project files ----
COPY . /app

# ---- Install Python dependencies ----
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ---- Expose application port ----
EXPOSE 5000

# ---- Run the game ----
CMD ["python", "MainGame.py"]




