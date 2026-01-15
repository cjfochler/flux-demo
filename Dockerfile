FROM python:3.12-slim

WORKDIR /app
COPY src/ src/
RUN pip install fastapi uvicorn

ENV APP_VERSION=local
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
