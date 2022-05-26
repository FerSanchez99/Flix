import DBpsql as db
class login:
    def auth(self, email, password):
        ans = db.dbpsql().getPassword(email)
        if ans != False:
            return password == ans
        return False