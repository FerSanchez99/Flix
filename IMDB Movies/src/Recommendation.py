import DBpsql

class recommendation:
    def setPreferences(self, user, cat1, cat2, cat3, ordered):
        pk = recommendation().calculatePK(cat1, cat2, cat3)
        DBpsql.db.savePreferences(user, pk, ordered)

    def getPK(self, user):
        return DBpsql.db.getPreferenceKey(user)

    def getOrderedSetting(self,user):
        return DBpsql.db.getOrderedSetting(user)

    def getMoviesRec(self, pk, ordered):
        return DBpsql.db.getMoviesRec(pk, ordered)

    def calculatePK(self, cat1, cat2, cat3):
        return round(((int(cat1) * int(cat2) * int(cat3)) % 5) + 1)

    def getUser(self):
        return DBpsql.db.current_user

    @staticmethod
    def isMoviesTableEmpty():
        return DBpsql.db.isMoviesTableEmpty()