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

class dbpsql:
    current_user = None
    def getPassword(self, email):
        global session
        query = session.execute(f"SELECT password FROM users WHERE email = '{email}'").fetchone()
        if query != None: global current_user; current_user=query[0]; return query[0]
        return False

    def register(self, email, password):
        global session
        session.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")