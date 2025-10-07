# Use a lightweight Python base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    gunicorn \
    psycopg2-binary

# Copy project files
COPY . .

# Collect static files (no user input)
RUN python manage.py collectstatic --noinput

# Expose the app port
EXPOSE 8000

# Run Django with Gunicorn in production
CMD ["gunicorn", "real_estate_api.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=4"]
