
# Math Operations Microservice

## Description

A FastAPI microservice to compute:
- Power
- Fibonacci
- Factorial

All requests are logged in a SQLite database.

## Running

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

- POST /math/pow
- POST /math/fibonacci
- POST /math/factorial
- GET /health
