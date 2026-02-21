FROM python:3.10.12

WORKDIR /app

# Copy entire src directory (recommended)
COPY ./src /app/src
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8010

# Run with gunicorn (4 workers)
CMD ["gunicorn", "src.app.app:app", "-b", "0.0.0.0:8010", "-w", "4"]