FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt from the estate_service directory
COPY estate_service/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the app code
COPY estate_service/app/ /app

EXPOSE 8000
CMD ["uvicorn", "estate_service.app.main:app", "--host", "0.0.0.0", "--port", "8000"]