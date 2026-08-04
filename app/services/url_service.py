from sqlalchemy.orm import Session

from app.models.url import URL
from app.services.shortener import generate_short_code


def create_short_url(db: Session, long_url: str):

    # Check if URL already exists
    existing = (
        db.query(URL)
        .filter(URL.long_url == long_url)
        .first()
    )

    if existing:
        return existing

    # Generate unique code
    while True:

        code = generate_short_code()

        duplicate = (
            db.query(URL)
            .filter(URL.short_code == code)
            .first()
        )

        if not duplicate:
            break

    url = URL(
        long_url=long_url,
        short_code=code,
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url