from pydantic import BaseModel, EmailStr, validator, ConfigDict
from typing import Optional
from datetime import datetime
import re

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password1: str
    password2: str
    
    @validator('username')
    def validate_username(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Username cannot be empty")
        # Remove spaces from username
        return "".join(v.split(" "))
    
    @validator('email') 
    def validate_email(cls, v):
        # Remove spaces from email
        return "".join(str(v).split(" "))
    
    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError("Passwords don't match")
        return v
    
    @validator('password1')
    def validate_password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        
        # Password strength validation (matching Django logic)
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        digits = "0123456789"
        
        status_queue = [0, 0, 0, 0]  # [lower, upper, symbols, digits]
        
        for char in v:
            if char in lower:
                status_queue[0] = 1
            elif char in upper:
                status_queue[1] = 1
            elif char in symbols:
                status_queue[2] = 1
            elif char in digits:
                status_queue[3] = 1
            
            if status_queue == [1, 1, 1, 1]:
                break
        
        error_messages = []
        if status_queue[0] == 0:
            error_messages.append("At least one lowercase letter is needed")
        if status_queue[1] == 0:
            error_messages.append("At least one uppercase letter is needed")
        if status_queue[2] == 0:
            error_messages.append("At least one symbol is needed")
        if status_queue[3] == 0:
            error_messages.append("At least one digit is needed")
        
        if error_messages:
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