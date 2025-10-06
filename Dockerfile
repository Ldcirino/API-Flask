FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=manage.py
ENV FLASK_ENV=production

CMD ["gunicorn", "manage:app", "-b", "0.0.0.0:5000", "--workers", "2"]
