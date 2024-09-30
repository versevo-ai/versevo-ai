import os
from supabase import create_client, Client
from subscription.schema.waitlist_schema import WaitlistSchema
from tomlkit import table

url: str = os.environ.get("SUPABASE_URL") # type: ignore
key: str = os.environ.get("SUPABASE_KEY") # type: ignore
table_name: str = os.environ.get("SUPABASE_TABLE_NAME") # type: ignore

supabase: Client = create_client(url, key) # type: ignore

def get_supabase():
    response = supabase.table(table_name).select("*").execute()
    return response

def post_supabase(data: WaitlistSchema):
    response = (
        supabase
        .table(table_name)
        .insert({"email_id": data.email_id,
                 "created_at": data.created_at})
    )
    return response

def check_supabase(email: str) -> bool:
    response = (
      supabase.table(table_name)
      .select("email_id")
      .eq("email_id", email)
      .execute()
    )
    print(response)
    return bool(response.data)