# Database Design

## Overview

The application uses PostgreSQL as its relational database management system. URL mappings are stored in a single table named **urls**.

---

## Database

```
url_shortener_db
```

---

## Table Structure

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| long_url | String | Original URL |
| short_code | String | Unique Short Code |
| created_at | Timestamp | Record creation time |

---

## Entity Description

### id

Unique identifier for every URL entry.

---

### long_url

Stores the original URL submitted by the user.

Example:

```
https://www.google.com
```

---

### short_code

Stores the generated unique identifier.

Example:

```
Ab12Cd
```

---

### created_at

Stores the timestamp when the URL was created.

---

## Database Workflow

1. User submits a long URL.
2. Application checks whether the URL already exists.
3. If not found, a new short code is generated.
4. URL mapping is stored in PostgreSQL.
5. Future requests retrieve the original URL using the short code.

---

## Advantages

- Fast lookup using indexed short codes
- Reliable relational storage
- Easy scalability
- ACID-compliant transactions