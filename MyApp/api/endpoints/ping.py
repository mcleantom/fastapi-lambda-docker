from fastapi import APIRouter

__all__ = ["router"]

router = APIRouter(prefix="/ping")


@router.get("")
def ping():
    return "pong"
