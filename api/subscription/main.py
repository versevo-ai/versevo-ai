import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from subscription.router.waitlist import waitlist_router
from subscription.router.health import health_router


app = FastAPI()
templates = Jinja2Templates(directory='subscription/templates')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Returning the index.html file
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(waitlist_router, prefix="/waitlist", tags=["waitlist"])
app.include_router(health_router, prefix="/health", tags=["health"])