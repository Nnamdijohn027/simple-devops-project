FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV APP_VERSION=1.0.0
ENV ENV=production

EXPOSE 5000

CMD ["python", "app.py"]
