# FastAPI Docker Production Deployment

A production-ready FastAPI application containerized with Docker, featuring Gunicorn + Uvicorn workers for optimal performance, best practices, and rapid deployment.

---

## 🗂️ Repository Structure

```
fastapi-docker-production/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── routes/
│       ├── __init__.py
│       ├── items.py
│       └── users.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_routes.py
├── gunicorn_conf.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 Features

- 🐳 **Docker containerization** for consistent deployments
- 🚀 **Gunicorn + Uvicorn** workers for high concurrency and async performance
- 🔒 Non-root user execution for enhanced security
- 📦 Multi-stage Docker build for small, secure images
- 🛡️ Environment-based configuration via `.env`
- 📊 Health check endpoints for monitoring and orchestration
- 🧪 Built-in test suite (pytest)
- 📝 Comprehensive logging and CORS support

---

## 🏁 Quick Start — Dockerized Production

### Prerequisites

- Docker and Docker Compose installed

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd fastapi-docker-production
```

### 2. Configure Environment

Copy the example environment file and edit as needed:

```bash
cp .env.example .env
# Edit .env with your preferred editor
```

### 3. Build & Run with Docker Compose

```bash
docker-compose up --build
```

- The API will be available at: [http://localhost:8000](http://localhost:8000)
- Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/health](http://localhost:8000/health)

### 4. View Logs

```bash
docker-compose logs -f
```

---

## 🧑‍💻 Local Development (Without Docker)

### 1. Create and Activate Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Copy .env.example to .env and edit as needed.

### 4. Run the App with Hot Reload

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🔍 API Endpoints

| Method | Endpoint           | Description      |
|--------|--------------------|------------------|
| GET    | `/`                | Welcome message  |
| GET    | `/health`          | Health check     |
| GET    | `/items/`          | List items       |
| POST   | `/items/`          | Create item      |
| GET    | `/items/{item_id}` | Get item by ID   |
| DELETE | `/items/{item_id}` | Delete item by ID|
| GET    | `/users/`          | List users       |
| POST   | `/users/`          | Create user      |
| GET    | `/users/{user_id}` | Get user by ID   |
| DELETE | `/users/{user_id}` | Delete user by ID|

---

## 🐳 Dockerfile Highlights

- **Multi-stage build**: Installs dependencies in a builder container, then copies only needed files to final image.
- **Non-root user**: Avoids running app as root in the container.
- **Healthcheck**: Verifies API liveness.
- **Gunicorn + Uvicorn**: Runs the app with async workers for production.

---

## 🛠️ Docker Compose

- **Service `web`**: Runs the FastAPI app, exposes port 8000, uses environment from `.env`
- **Service `db` (optional)**: Example PostgreSQL service, uncomment to enable
- **Volumes**: Persists database data

---

## 📝 Configuration Notes

- **Gunicorn config** (`gunicorn_conf.py`):  
  - Uses Uvicorn workers
  - Number of workers set via `WORKERS` env variable (default: `(CPU * 2) + 1`)
  - Logs to stdout

- **Environment variables**:  
  - Set via `.env` or passed at runtime
  - Examples: `DEBUG`, `HOST`, `PORT`, `WORKERS`, `DATABASE_URL`, `LOG_LEVEL`

---

## 🚦 Health Checks & Monitoring

- `/health`: Basic health check (status, timestamp, version)
- `/health/detailed`: System info if `psutil` is installed

---

## 🔒 Security Best Practices

- Runs as non-root user in Docker for security
- Sensitive config via environment variables (never commit secrets)
- Regularly update dependencies
- Use reverse proxy (Nginx) for SSL in production
- Set secure CORS policy for production

---

## 🧪 Running Tests

```bash
# With Docker Compose
docker-compose exec web pytest

# Or locally (after installing requirements)
pytest tests/
```

---

## 🛠️ Troubleshooting

- **Port in use**:  
  Use a different host port with `-p 8080:80`
- **Container not starting**:  
  Check logs: `docker-compose logs -f`
- **Health check failing**:  
  Ensure app is running and accessible at `/health`
- **Permission issues**:  
  Build and run as admin, or ensure volumes are writable

---

## 🏎️ Performance & Scaling

- Tune `WORKERS` in `.env` or Docker Compose for your hardware
- Use Docker Compose scaling:  
  `docker-compose up -d --scale web=4`
- For more, use Kubernetes with liveness/readiness probes

---

## 🛡️ Production Deployment

- **Build image**:  
  `docker build -t my-fastapi-app .`
- **Run container**:  
  `docker run -d -p 80:80 --name fastapi-app my-fastapi-app`
- **With Compose**:  
  `docker-compose up --build`

---

## 💡 Pro Tips

- Use `psutil` for detailed health checks (add to requirements if needed)
- Use `.dockerignore` to keep images slim
- Always test locally before deploying to production

---

## 📝 License

MIT License — Free to use for learning and production deployments.

---

**Your FastAPI app is now ready to deploy at scale with Docker, Gunicorn, and Uvicorn! 🚀**
