from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

# Create a local Base for models (independent of database.py)
Base = declarative_base()

class User(Base):
    """
    SQLAlchemy User model that maps to Django's NewUser model
    """
    __tablename__ = "users_newuser"
    
    # Core fields from AbstractUser
    username = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=True)
    password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    date_joined = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Custom fields from NewUser
    Access_Token = Column(String, nullable=True)
    Refresh_Token = Column(String, nullable=True)
    Blacklisted = Column(Boolean, default=False)
    private_key = Column(String, nullable=True)
    public_key = Column(String, nullable=True)
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"