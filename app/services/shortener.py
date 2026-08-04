import secrets
import string

from app.core.config import settings


ALPHABET = string.ascii_letters + string.digits


def generate_short_code() -> str:
    return "".join(
        secrets.choice(ALPHABET)
        for _ in range(settings.SHORT_CODE_LENGTH)
    )