import DBpsql as db
class Login():
    @staticmethod
    def auth(user, password):
        ans = db.DBpsql.getPassword(user)
        if not ans:
            return password == ans
        return False
     
