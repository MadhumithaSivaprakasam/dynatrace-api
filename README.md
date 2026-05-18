# 🔍 Dynatrace Problem Monitor

A lightweight Flask-based microservice that connects to the Dynatrace API v2 to fetch and display active problems from your Dynatrace environment.

---

## 📌 Features

- REST API built with Flask
- Fetches real-time active problems from Dynatrace
- Secure API token loading via environment variables
- JSON response via `/problems` endpoint
- Flask-based microservice architecture

---

## 🗂️ Project Structure

```text
dynatrace/
├── service.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MadhumithaSivaprakasam/dynatrace-api.git
cd dynatrace
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

Create a `.env` file in the root directory:

```text
DYNATRACE_API_TOKEN=your_dynatrace_api_token
```

⚠️ Never upload `.env` to GitHub.

---

## 🚀 Run the Microservice

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
| GET | `/` | Health check endpoint |
| GET | `/problems` | Returns active Dynatrace problems |

---

## 📌 Example Endpoint

```text
http://127.0.0.1:5000/problems
```

---

## 🔄 Project Workflow

```text
Browser / Client
        ↓
Flask Microservice
        ↓
Dynatrace Problems API
        ↓
JSON Response
```

---

## 🛡️ Security

API tokens are securely stored using environment variables through a `.env` file instead of hardcoding secrets inside source code.

---

## 🧰 Technologies Used

- Python
- Flask
- requests
- python-dotenv
- REST API
- JSON
