import DBpsql as db
class signUp:
    def registerUser(self, email, password):
        db.dbpsql().register(email, password)