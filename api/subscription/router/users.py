from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session # type: ignore
from typing import List
from datetime import timedelta
import os

from subscription.database import get_db
from subscription.schemas.user_schema import (
    UserCreate, UserResponse, UserUpdate, UserLogin, Token
)
from subscription.models.user import User
from subscription.auth.auth import (
    authenticate_user, get_current_active_user, get_password_hash,
    create_access_token, create_refresh_token, ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()

@router.post("/register", response_model=dict)
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    try:
        # Check if username already exists
        existing_user = db.query(User).filter(User.username == user_data.username).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        # Check if email already exists
        existing_email = db.query(User).filter(User.email == user_data.email).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        # Create new user
        hashed_password = get_password_hash(user_data.password1)

        # Check if this is a superuser
        is_superuser = user_data.email == os.getenv("SUPERUSER_EMAIL")

        db_user = User(
            username=user_data.username,
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            password=hashed_password,
            is_superuser=is_superuser,
            is_staff=is_superuser
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return {
            "Status": "CREATED",
            "message": f"User {user_data.username} created successfully",
            "data": {
                "username": db_user.username,
                "email": db_user.email,
                "is_superuser": db_user.is_superuser
            }
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )

@router.post("/login", response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Authenticate user and return JWT tokens."""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.Blacklisted:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is blacklisted"
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token = create_refresh_token(data={"sub": user.username})

    # Update user tokens in database
    user.Access_Token = access_token
    user.Refresh_Token = refresh_token
    user.last_login = db.query(User).filter(User.username == user.username).first().last_login

    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """Get current user information."""
    return current_user

@router.get("/profile", response_model=dict)
async def get_user_profile(current_user: User = Depends(get_current_active_user)):
    """Get user profile with serialized data (Django-style response)."""
    return {
        "Message": "FETCHED",
        "Data": {
            "username": current_user.username,
            "email": current_user.email,
            "first_name": current_user.first_name,
            "last_name": current_user.last_name,
            "is_active": current_user.is_active,
            "is_staff": current_user.is_staff,
            "is_superuser": current_user.is_superuser,
            "date_joined": current_user.date_joined.isoformat() if current_user.date_joined else None,
            "last_login": current_user.last_login.isoformat() if current_user.last_login else None,
            "Blacklisted": current_user.Blacklisted
        }
    }

@router.put("/update", response_model=dict)
async def update_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update user information."""
    try:
        # Check if new username already exists (if provided)
        if user_update.new_username and user_update.new_username != current_user.username:
            existing_user = db.query(User).filter(User.username == user_update.new_username).first()
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists"
                )
            current_user.username = user_update.new_username

        # Update other fields if provided
        if user_update.email and user_update.email != current_user.email:
            # Check if email already exists
            existing_email = db.query(User).filter(User.email == user_update.email).first()
            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
            current_user.email = user_update.email

        if user_update.first_name is not None:
            current_user.first_name = user_update.first_name

        if user_update.last_name is not None:
            current_user.last_name = user_update.last_name

        db.commit()
        db.refresh(current_user)

        return {
            "Status": "UPDATED",
            "message": "User updated successfully",
            "data": {
                "username": current_user.username,
                "email": current_user.email,
                "first_name": current_user.first_name,
                "last_name": current_user.last_name
            }
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating user: {str(e)}"
        )

@router.delete("/delete", response_model=dict)
async def delete_user(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete user account (only if blacklisted)."""
    try:
        if not current_user.Blacklisted:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User must be blacklisted before deletion"
            )

        username = current_user.username
        db.delete(current_user)
        db.commit()

        return {
            "Status": "DELETED",
            "message": f"User {username} has been deleted successfully"
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting user: {str(e)}"
        )

@router.post("/logout", response_model=dict)
async def logout_user(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Logout user by clearing tokens."""
    try:
        # Clear tokens
        current_user.Access_Token = None
        current_user.Refresh_Token = None
        db.commit()

        return {
            "Status": "SUCCESS",
            "message": "User logged out successfully"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error logging out user: {str(e)}"
        )