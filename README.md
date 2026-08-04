# 🔗 URL Shortener API

A professional URL Shortener REST API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The application allows users to shorten long URLs into unique short codes and automatically redirects users to the original URL.

---

## 📌 Features

- Shorten long URLs
- Automatic redirection using short codes
- PostgreSQL database integration
- SQLAlchemy ORM
- RESTful API design
- Interactive Swagger UI
- Automated testing using Pytest
- Continuous Integration using GitHub Actions
- Environment variable configuration

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| Pytest | Testing |
| GitHub Actions | Continuous Integration |
| Python 3.13 | Programming Language |

---

## 📁 Project Structure

```text
url-shortner-api/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── middleware/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── docs/
├── tests/
├── .github/
├── README.md
├── requirements.txt
├── pytest.ini
└── .env.example
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/psnc2504-wq/url-shortener-api.git
```

Move into the project directory:

```bash
cd url-shortener-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Variables

Create a `.env` file:

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

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

## 📡 API Endpoints

### Create Short URL

**POST**

```
/shorten
```

Example Request

```json
{
    "url":"https://www.google.com"
}
```

Example Response

```json
{
    "short_url":"http://localhost:8000/Ab12Cd"
}
```

---

### Redirect

**GET**

```
/{short_code}
```

Example

```
GET /Ab12Cd
```

Automatically redirects to the original URL.

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🔄 Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Starts PostgreSQL
- Executes Pytest
- Verifies every push to the repository

---

## 🚀 Future Improvements

- URL analytics
- Custom aliases
- User authentication
- QR code generation
- URL expiration
- Rate limiting
- Docker deployment
- Cloud deployment (AWS/Azure)

---

## 👨‍💻 Author

**Surya Narayan**

Electronics & Communication Engineering

Backend Development | Python | FastAPI | PostgreSQL