FROM python:3.11-slim

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .


CMD ["gunicorn", "--bind", "0.0.0.0:9000", "stripe_project.wsgi"]