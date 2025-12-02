# 🧾 Digital Signature Service (Toy Project)

> **Mock implementation** of a trusted digital signature platform for educational and testing purposes.
> Built with **Python 3.12**, **PostgreSQL**, **RabbitMQ**, **Redis**, and a minimal **frontend SPA**.
> ⚠️ *This project is for demonstration only — no real cryptographic operations are performed.*

---

## 📖 Overview

This project simulates a **qualified digital signature service**, capable of:

* Receiving signing requests (documents or payloads).
* Generating **mock signatures** and returning valid-like responses.
* Publishing and consuming service events via **RabbitMQ**.
* Persisting request/response metadata in **PostgreSQL**.
* Using **Redis** for caching and request throttling.

Focus: **system integration**, **asynchronous design**, and **load testing** — not real cryptography.

---

## 🧩 Components

| Component             | Description                                           |
| --------------------- | ----------------------------------------------------- |
| **Backend (FastAPI)** | Handles signing requests, responses, and OpenAPI docs |
| **PostgreSQL**        | Persistent data storage                               |
| **RabbitMQ**          | Event bus for asynchronous message passing            |
| **Redis**             | In-memory cache layer                                 |
| **Frontend SPA**      | Minimal UI for interacting with backend               |
| **Locust Tests**      | External project for load and performance testing     |

---

## 🏗 Architecture (Conceptual)

```
      ┌─────────────┐
      │  Frontend   │
      └──────┬──────┘
             │
             ▼
      ┌─────────────┐
      │  Backend    │
      └───┬─────┬───┘
          │     │
 ┌────────┘     └────────┐
 │                       │
 ▼                       ▼
PostgreSQL              Redis
 │
 ▼
RabbitMQ
```

---

## ⚙️ Setup & Development

### Prerequisites

* Python **3.12+**
* Docker & Docker Compose
* (Optional) Node.js — if modifying frontend

### Build & Run

```bash
# Copy example enviromnent variables
cp .env.example .env

# Clean Docker environment
sudo docker system prune -af

# Build and run all services
sudo docker-compose up --build

# Stop and remove containers, networks, volumes
sudo docker-compose down --v
```

Access backend: [http://localhost:8000](http://localhost:8000)
OpenAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing & Database Access

Run tests inside the backend container:

```bash
sudo docker exec -it digital-signature-service_backend_1 uv run pytest
```

Access PostgreSQL database:

```bash
sudo docker exec -it digital-signature-service_db_1 psql -U postgres -d digital_signature_service
```

For load testing, use the separate **`locust-tests/`** project:

```bash
cd ../locust-tests
locust -f locustfile.py --host=http://localhost:8000
```

Locust web UI: [http://localhost:8089](http://localhost:8089)

---

## 🧱 Project Structure

```
digital-signature-service/
├── backend/           # FastAPI backend + services + tests
├── frontend/          # Minimal SPA for UI interaction
├── docker-compose.yml # Docker setup
├── scripts/           # Utility scripts (SQL, bash)
└── README.md
```

---

## 🧠 Notes

* This service **imitates real-world signing**: response timing, async processing, and persistence.
* All sensitive operations are **mocked or simulated**.
* OpenAPI documentation is automatically available via FastAPI (`/docs`).

---

## 📜 License

MIT License © 2025 — Created for educational and research purposes.
