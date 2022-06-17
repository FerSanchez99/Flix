import DBpsql as db
class signUp:
    def register(self, email, password):
        db.dbpsql().registerUser(email, password)