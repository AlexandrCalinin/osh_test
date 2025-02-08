FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt from the auth_service directory
COPY auth_service/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the app code
COPY auth_service/app/ /app

EXPOSE 8001
CMD ["uvicorn", "auth_service.app.main:app", "--host", "0.0.0.0", "--port", "8001"]