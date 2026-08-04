from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.url import URLRequest, URLResponse
from app.services.url_service import create_short_url
from app.core.config import settings

router = APIRouter(
    prefix="/shorten",
    tags=["URL Shortener"]
)


@router.post(
    "",
    response_model=URLResponse
)
def shorten_url(
    request: URLRequest,
    db: Session = Depends(get_db)
):

    url = create_short_url(
        db=db,
        long_url=str(request.url)
    )

    return URLResponse(
        short_url=f"{settings.BASE_URL}/{url.short_code}"
    )