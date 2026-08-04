# System Architecture

## Overview

The URL Shortener API follows a layered architecture to ensure modularity, maintainability, and scalability. Each layer has a specific responsibility, making the application easier to develop, test, and extend.

---

## Architecture Diagram

```
                Client
                   │
                   ▼
            FastAPI Application
                   │
                   ▼
              API Endpoints
                   │
                   ▼
            Business Services
                   │
                   ▼
            SQLAlchemy ORM
                   │
                   ▼
              PostgreSQL
```

---

## Architecture Components

### Client Layer

The client interacts with the application using HTTP requests. Clients may include web browsers, REST clients such as Postman, or any application capable of consuming REST APIs.

---

### FastAPI Application

FastAPI serves as the entry point of the application. It receives incoming requests, validates request data, and forwards the request to the appropriate API endpoint.

---

### API Layer

The API layer exposes REST endpoints responsible for:

- Creating shortened URLs
- Redirecting users to the original URL

---

### Service Layer

The service layer contains the application's business logic. It is responsible for:

- Generating unique short codes
- Checking for duplicate URLs
- Communicating with the database layer

---

### Database Layer

SQLAlchemy ORM handles communication with PostgreSQL, allowing Python objects to be stored and retrieved without writing raw SQL queries.

---

## Request Flow

1. Client sends a POST request with a long URL.
2. FastAPI validates the request.
3. The service layer generates a unique short code.
4. SQLAlchemy stores the URL mapping in PostgreSQL.
5. The shortened URL is returned to the client.
6. When the shortened URL is accessed, the application retrieves the original URL from the database and redirects the client.