from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.url import URL

router = APIRouter(
    tags=["Redirect"]
)


@router.get("/{short_code}")
def redirect(
    short_code: str,
    db: Session = Depends(get_db)
):

    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(
        url=url.long_url,
        status_code=307
    )