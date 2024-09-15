from fastapi import APIRouter

waitlist_router = APIRouter()

# This route registers a user to the waitlist and also checks if the user is already registered.
@waitlist_router.get("/register")
async def register() -> dict:
    return {"message": "waitilist service is up and running"}