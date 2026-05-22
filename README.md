# 🔍 Dynatrace Problem Monitor

A Flask-based microservice that integrates with the Dynatrace API v2 to fetch and manage monitoring problems.

---

## 📌 Features

- Flask-based REST microservice
- Dynatrace Problems API integration
- Fetch all active problems
- Fetch specific problem details
- Structured backend architecture
- Response transformation using models
- Secure API token handling using `.env`
- Unit testing and integration testing

---

## 🗂️ Project Structure

```text
dynatrace/
│
├── app/
│   ├── auth/
│   │   └── auth.py
│   │
│   ├── models/
│   │   └── problem_model.py
│   │
│   ├── routes/
│   │   └── problems.py
│   │
│   ├── services/
│   │   └── dynatrace_service.py
│   │
│   └── tests/
│       ├── test_unit.py
│       └── test_integration.py
│
├── service.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/MadhumithaSivaprakasam/dynatrace-api.git
cd dynatrace-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configure Environment Variables

Create a `.env` file:

```text
DYNATRACE_API_TOKEN=your_api_token
```

⚠️ Never upload `.env` to GitHub.

---

## 🚀 Run the Application

```bash
python service.py
```

Server runs at:

```text
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/problems` | Fetch all problems |
| GET | `/problems/<problem_id>` | Fetch specific problem details |

---

## 🧪 Running Tests

```bash
pytest app/tests
```

---

## 🛡️ Security

API tokens are securely stored using environment variables and loaded through `.env`.

---

## 🧰 Technologies Used

- Python
- Flask
- Requests
- Pytest
- REST API
- JSON
- python-dotenv
