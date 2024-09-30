from pydantic import BaseModel,Field

class WaitlistSchema(BaseModel):
    email_id: str = Field(...)
    created_at: str = Field(...)

    class Config:
        orm_mode = True