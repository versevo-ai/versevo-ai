from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/check")
async def health():
    return {"status": "ok"}