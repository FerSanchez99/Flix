from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movies.models import get_postgres_uri

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()

def create(email, password):
    session.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")
    
def read(email, password):
    query = session.execute(f"SELECT email, password FROM users WHERE email = '{email}'").fetchone()
    if query != None and query[0] == email and query[1] == password: return True
    return False