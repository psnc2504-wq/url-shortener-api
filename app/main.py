from fastapi import FastAPI

from app.core.config import settings

from app.database.base import Base
from app.database.session import engine

from app.models.url import URL

from app.api.shorten import router as shorten_router
from app.api.redirect import router as redirect_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

Base.metadata.create_all(bind=engine)

app.include_router(shorten_router)
app.include_router(redirect_router)


@app.get("/")
async def root():
    return {
        "service": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running",
    }