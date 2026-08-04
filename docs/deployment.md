# Deployment Guide

## Prerequisites

Before running the application, ensure the following software is installed:

- Python 3.13 or later
- PostgreSQL
- Git

---

## Clone Repository

```bash
git clone https://github.com/psnc2504-wq/url-shortener-api.git
```

Move into the project directory:

```bash
cd url-shortener-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
APP_NAME=URL Shortener API
VERSION=1.0.0

DB_HOST=localhost
DB_PORT=5432
DB_NAME=url_shortener_db
DB_USER=postgres
DB_PASSWORD=your_password

BASE_URL=http://localhost:8000
SHORT_CODE_LENGTH=6
```

---

## Configure PostgreSQL

Create a PostgreSQL database:

```
url_shortener_db
```

Ensure the credentials in `.env` match your PostgreSQL configuration.

---

## Start the Application

```bash
uvicorn app.main:app --reload
```

Application:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

## Run Automated Tests

```bash
pytest
```

---

## Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Starts PostgreSQL
- Runs automated tests
- Validates every push to the repository

---

## Future Deployment Options

The application can be deployed using:

- Docker
- Render
- Railway
- AWS EC2
- Azure App Service
- Google Cloud Run