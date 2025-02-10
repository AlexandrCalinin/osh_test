FROM python:3.13-slim

WORKDIR /estate_service

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./estate_service /estate_service/estate_service

ENV PYTHONPATH=/estate_service

RUN pip install --no-cache-dir --upgrade -r estate_service/requirements.txt

CMD ["uvicorn", "estate_service.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
