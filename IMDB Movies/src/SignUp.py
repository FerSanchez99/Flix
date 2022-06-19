import DBpsql

class signUp:
    def register(self, email, password):
        DBpsql.db.registerUser(email, password)