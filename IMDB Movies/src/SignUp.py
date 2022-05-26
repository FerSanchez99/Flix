import DBpsql as db
class SignUp():
    @staticmethod
    def registerUser(user, password):
        db.DBpsql.register(user,password)
        
     
