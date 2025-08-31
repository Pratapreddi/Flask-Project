FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose container port
EXPOSE 5000

# Run app with Gunicorn on port 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

