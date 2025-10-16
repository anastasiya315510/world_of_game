FROM python:3.11-slim

WORKDIR /app

COPY . /app
COPY Scores.txt /Scores.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run main.py (CLI game launches Flask in background)
CMD ["python", "MainGame.py"]



