from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movies.models import get_postgres_uri
from DBInterface import DBInterface

Session = sessionmaker(bind=create_engine(get_postgres_uri()))
session = Session()

class dbpsql(DBInterface):
    def __init__(self):
        self.current_user = None

    def getPassword(self, email):
        query = session.execute(f"SELECT user_id, password FROM users WHERE email = '{email}'").fetchone()
        if query != None: self.current_user=query[0]; return query[1]
        return False

    def getPreferenceKey(self, user_id):
        query = session.execute(f"SELECT preference_key FROM users WHERE user_id = '{user_id}'").fetchone()
        if query != None: return query[0]
        return False

    def getOrderedSetting(self, user_id):
        query = session.execute(f"SELECT ordered_rec FROM users WHERE user_id = '{user_id}'").fetchone()
        if query != None: return query[0]
        return False

    def registerUser(self, email, password):
        session.execute(f"INSERT INTO users (email, password, ordered_rec) VALUES ('{email}', '{password}', 'true')")
        session.commit()

    def savePreferences(self, user_id, preference_key, ordered):
        session.execute(f"UPDATE users SET preference_key={preference_key} WHERE user_id='{user_id}'")       
        session.execute(f"UPDATE users SET ordered_rec={ordered} WHERE user_id='{user_id}'")       
        session.commit()

    def getMoviesRec(self, pk, ordered):
        if ordered:
            query = session.execute(f"SELECT movie_title, year, rating, link FROM movies WHERE preference_key={pk} LIMIT 10") 
        else:
            query = session.execute(f"SELECT movie_title, year, rating, link FROM movies WHERE preference_key={pk} ORDER BY rating ASC LIMIT 10")
        if query != None: return list(query)
        return False   
        
    @staticmethod
    def isMoviesTableEmpty():
        query = session.execute("select COUNT(*) from movies")
        if int(query.first()[0]) > 0: return False
        return True

db = dbpsql()