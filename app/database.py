import psycopg2
from psycopg2.extras import RealDictCursor
from app.config import DATABASE_URL


def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
