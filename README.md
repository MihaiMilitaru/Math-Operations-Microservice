# 📐 Math Operations Microservice

This project is a lightweight **Python microservice** built using **FastAPI**, providing a RESTful API for performing basic mathematical operations:

- Power (`pow`)
- Fibonacci (`n-th`)
- Factorial

All operations are persisted in a **SQLite** database. This is designed following **microservice best practices** and can be easily extended or containerized.

---

## 🚀 Features

- ⚡ FastAPI (async, modern web framework)
- 💾 SQLite for simple persistence
- 🔌 RESTful API (OpenAPI/Swagger auto-generated)
- ♻️ Modular architecture (MVC/MVCS)
- 🔒 API key-based security placeholder (optional)
- 🐳 Docker support

---

## 📁 Project Structure

```
math_service/
├── app/
│   ├── main.py              # Entry point
│   ├── controllers.py       # Route definitions
│   ├── services.py          # Business logic
│   ├── schemas.py           # Request validation
│   ├── database.py          # DB models and session
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ✅ Requirements

- Python 3.10+
- pip
- (Optional) Docker

---

## 🔧 Setup Instructions

### 🔹 Run Locally

1. **Clone and enter project**

    ```bash
    unzip math_service_project.zip
    cd math_service
    ```

2. **Create and activate virtual environment** (optional)

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**

    ```bash
    uvicorn app.main:app --reload
    ```

5. **Access the API docs**

    Open your browser and visit:

    ```
    http://127.0.0.1:8000/docs
    ```

---

### 🐳 Run with Docker

1. **Build the image**

    ```bash
    docker build -t math_service .
    ```

2. **Run the container**

    ```bash
    docker run -p 8000:8000 math_service
    ```

---

## 🧪 Example API Requests

### ➕ Power

**POST** `/math/pow`

```json
{
  "base": 2,
  "exponent": 3
}
```

**Response**
```json
{
  "result": 8.0
}
```

---

### 🔢 Fibonacci

**POST** `/math/fibonacci`

```json
{
  "n": 7
}
```

**Response**
```json
{
  "result": 13
}
```

---

### ✖️ Factorial

**POST** `/math/factorial`

```json
{
  "n": 5
}
```

**Response**
```json
{
  "result": 120
}
```

---

## 🧠 Design Notes

- Follows **MVCS** architecture for clean separation of concerns
- Each request is logged with inputs and outputs
- Easy to extend: just add new service logic + route
- Can be integrated with Redis (caching), Kafka (logging), or Prometheus (monitoring)


