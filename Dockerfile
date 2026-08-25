FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3","app.py"]
LABEL org.opencontainers.image.source="https://github.com/justinmihigo/docker-demo"
LABEL org.opencontainers.image.description="My container image"
LABEL org.opencontainers.image.licenses=MIT
