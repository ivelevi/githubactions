FROM python:3.9

# Create a non-root user
RUN groupadd -r myuser && useradd -r -g myuser myuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .


CMD ["python", "app.py"]