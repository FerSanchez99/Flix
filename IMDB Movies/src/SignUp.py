import DBpsql as db
class signUp:
    def register(email, password):
        db.dbpsql.registerUser(email, password)