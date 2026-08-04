from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "URL Shortener API")
    VERSION = os.getenv("VERSION", "1.0.0")

    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "url_shortener_db")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
    SHORT_CODE_LENGTH = int(os.getenv("SHORT_CODE_LENGTH", 6))


settings = Settings()