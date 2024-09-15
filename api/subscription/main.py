from fastapi import FastAPI
from subscription.router.waitlist import waitlist_router
from subscription.router.health import health_router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(waitlist_router, prefix="/waitlist", tags=["waitlist"])
app.include_router(health_router, prefix="/health", tags=["health"])