from fastapi import APIRouter

from .endpoints import ping

__all__ = ["router"]

router = APIRouter()
router.include_router(ping.router, tags=["Router"])


@router.get("/")
def home():
    return "Hello World!"
