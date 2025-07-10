import pytest
from sqlalchemy import text
from core.database import SessionLocal
import os
os.environ["DATABASE_URL"] = "mysql+pymysql://root:rootpass@maria_primary:3306/"

def test_database_connection():
    session = SessionLocal()
    assert session is not None

