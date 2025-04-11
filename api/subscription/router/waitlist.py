import datetime
from fastapi import APIRouter
from subscription.database import check_supabase, post_supabase
from subscription.schema.waitlist_schema import WaitlistSchema

waitlist_router = APIRouter()

# This route registers a user to the waitlist and also checks if the user is already registered.
@waitlist_router.get("/register/health", response_model=dict)
async def register_health() -> dict:
    return {"message": "Waitlist service is up and running"}


@waitlist_router.post("/register")
async def register(email_id: str) -> dict:
    # Validate email using Pydantic schema
    if check_supabase(email_id):
        return {"message": "User already registered"}
    else:
        try:
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post_supabase(WaitlistSchema(email_id=email_id, created_at=created_at))
            return {"message": "User registered successfully"}
        except Exception as e:
            return {"message": "Error registering user"}