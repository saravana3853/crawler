import os
from supabase import create_client, Client
from supabase.client import ClientOptions

url: str = "https://qlwfizhalzjnkexrtyos.supabase.co"
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsd2ZpemhhbHpqbmtleHJ0eW9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTc5MjgxNjcsImV4cCI6MjAzMzUwNDE2N30.gy6BNYzZV8qVwSM6m4oU0fg5wh_FJgKRwjb4E5pLrjc'

supabase: Client = create_client(url, key,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))


def insert(news_header,rank=None,score=None,age=None):
    data = supabase.table("y-combinator-news").insert({"news_header":"Germany"}).execute()


def bulk_insert(news_data):
    data = supabase.table("y-combinator-news").insert(news_data).execute()

def search(query):
    data = supabase.table("y-combinator-news").select("*").text_search("title",query).execute()
    return data.data
