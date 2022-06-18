import DBpsql as db
class login:
    def auth(email, password):
        ans = db.dbpsql.getPassword(email)
        if ans != False:
            return password == ans
        return False