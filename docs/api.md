# API Documentation

## Base URL

```
http://localhost:8000
```

---

# POST /shorten

## Description

Creates a shortened URL from the supplied long URL.

---

## Request

```json
{
    "url":"https://www.google.com"
}
```

---

## Success Response

```json
{
    "short_url":"http://localhost:8000/Ab12Cd"
}
```

---

## Response Code

| Code | Description |
|------|-------------|
|200|URL shortened successfully|
|400|Invalid URL|
|500|Internal Server Error|

---

# GET /{short_code}

## Description

Redirects the user to the original URL associated with the provided short code.

---

## Example

```
GET /Ab12Cd
```

---

## Response

HTTP Redirect

```
302 Found
```

or

```
307 Temporary Redirect
```

depending on the redirect implementation.

---

## Response Codes

| Code | Description |
|------|-------------|
|302/307|Redirect Successful|
|404|Short URL not found|
|500|Internal Server Error|

---

## Interactive Documentation

FastAPI automatically generates Swagger documentation.

```
http://localhost:8000/docs
```