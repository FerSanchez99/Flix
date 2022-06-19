import DBpsql

class login:
    def auth(self, email, password):
        ans = DBpsql.db.getPassword(email)
        if ans != False: return password == ans
        return False