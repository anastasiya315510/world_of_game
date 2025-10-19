# Score.py
import os
import pymysql
from pymysql import Error

# Database credentials from environment variables
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "games")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")  # set in Docker Compose

def get_connection():
    """Return a MySQL connection"""


    conn = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        port=int(os.environ.get('DB_PORT', 3306))
    )


def init_db():
    """Create the table if it doesn't exist"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_scores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                score INT NOT NULL
            )
        """)
        conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def write_score(score: int):
    """Insert the score into the database"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users_scores (score) VALUES (%s)", (score,))
        conn.commit()
    except Error as e:
        print(f"Error writing score: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def read_score():
    """Return the latest score from the database, or 0 if none"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT score FROM users_scores ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        return result[0] if result else 0
    except Error as e:
        print(f"Error reading score: {e}")
        return 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
