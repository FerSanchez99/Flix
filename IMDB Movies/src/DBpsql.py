import psycopg2

class DBpsql():
    cur = None
    @staticmethod
    def connect():
        conn = psycopg2.connect(
        host="localhost",
        database="movies",
        user="movies",
        password="abc123")
        cur = conn.cursor

    def getPassword(user):
        cur.execute('SELECT password FROM Users WHERE email = user')