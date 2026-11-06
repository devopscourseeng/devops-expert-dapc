FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
ENV PORT=8000
EXPOSE 8000

# Render and other platforms set PORT; gunicorn listens on it.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} app:app"]
