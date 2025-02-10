FROM python:3.13-slim

WORKDIR /auth_service

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./auth_service /auth_service/auth_service

ENV PYTHONPATH=/auth_service

RUN pip install --no-cache-dir --upgrade -r auth_service/requirements.txt

CMD ["uvicorn", "auth_service.app.main:app", "--host", "0.0.0.0", "--port", "8001"]