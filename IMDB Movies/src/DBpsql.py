from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movies.models import get_postgres_uri

Session = sessionmaker(bind=create_engine(get_postgres_uri()))
session = Session()

current_user = None

class dbpsql:
    def getPassword(self, email):
        query = session.execute(f"SELECT user_id, password FROM users WHERE email = '{email}'").fetchone()
        if query != None: global current_user; current_user=query[0]; return query[1]
        return False

    def getPreferenceKey(self, user_id):
        query = session.execute(f"SELECT preference_key FROM users WHERE user_id = '{user_id}'").fetchone()
        if query != None: return query[0]
        return False

    def registerUser(self, email, password):
        session.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")
        session.commit()

    def savePreferences(self, user_id, preference_key):
        session.execute(f"UPDATE users SET preference_key={preference_key} WHERE user_id='{user_id}'")        
        session.commit()