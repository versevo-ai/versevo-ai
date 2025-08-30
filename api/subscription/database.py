import os
from supabase import create_client, Client
from subscription.schema.waitlist_schema import WaitlistSchema
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Supabase configuration (for waitlist)
url: str = os.environ.get("SUPABASE_URL") # type: ignore
key: str = os.environ.get("SUPABASE_KEY") # type: ignore
table_name: str = os.environ.get("SUPABASE_TABLE_NAME") # type: ignore

# Initialize Supabase client only if credentials are provided
supabase: Client = None
if url and key:
    supabase = create_client(url, key) # type: ignore

# PostgreSQL configuration (for user management)
DATABASE_URL = os.getenv("MAIN_DB")

if DATABASE_URL:
    # SQLAlchemy setup
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
else:
    # Fallback for when database is not configured
    engine = None
    SessionLocal = None
    Base = None

# Dependency for getting database session
def get_db():
    if SessionLocal is None:
        raise ValueError("Database not configured")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_supabase():
    if not supabase:
        raise ValueError("Supabase not configured")
    response = supabase.table(table_name).select("*").execute()
    return response

def post_supabase(data: WaitlistSchema):
    if not supabase:
        raise ValueError("Supabase not configured")
    response = (
        supabase
        .table(table_name)
        .insert({"email_id": data.email_id,
                 "created_at": data.created_at})
    )
    return response

def check_supabase(email: str) -> bool:
    if not supabase:
        return False
    response = (
      supabase.table(table_name)
      .select("email_id")
      .eq("email_id", email)
      .execute()
    )
    print(response)
    return bool(response.data)