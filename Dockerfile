FROM python:3.11-slim

WORKDIR /app

# Install all required backend dependencies
RUN pip install fastapi uvicorn requests pyotp websocket-client


COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
