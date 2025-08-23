import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from subscription.router.waitlist import waitlist_router
from subscription.router.health import health_router
from subscription.router.users import router as user_router


app = FastAPI(
    title="Versevo AI API",
    description="User management and subscription API for Versevo AI platform",
    version="1.0.0",
)

templates = Jinja2Templates(directory='subscription/templates')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Returning the index.html file
    return templates.TemplateResponse("index.html", {"request": request})

# Include routers
app.include_router(waitlist_router, prefix="/waitlist", tags=["waitlist"])
app.include_router(health_router, prefix="/health", tags=["health"]) 
app.include_router(user_router, prefix="/users", tags=["users"])