from pydantic import BaseModel, EmailStr, field_validator, validator, ConfigDict
from typing import Optional
from datetime import datetime
from ..utils.validators import validate_password_strength, clean_string, validate_username

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password1: str
    password2: str

    @field_validator('username')
    def validate_username_field(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Username cannot be empty")
        return clean_string(v)

    @field_validator('email')
    def validate_email_field(cls, v):
        return clean_string(str(v))

    @field_validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError("Passwords don't match")
        return v

    @field_validator('password1')
    def validate_password_strength_field(cls, v):
        is_valid, error_messages = validate_password_strength(v)
        if not is_valid:
            raise ValueError("; ".join(error_messages))
        return v

class UserUpdate(BaseModel):
    new_username: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    is_active: bool
    is_staff: bool
    is_superuser: bool
    date_joined: datetime
    last_login: Optional[datetime] = None
    Blacklisted: bool

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None