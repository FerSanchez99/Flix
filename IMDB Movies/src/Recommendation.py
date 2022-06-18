import DBpsql as db
class recommendation:
    def setPreferences(self, user, cat1, cat2, cat3):
        pk = recommendation().calculatePK(cat1, cat2, cat3)
        db.dbpsql().savePreferences(user, pk)

    def getPK(user):
        return db.dbpsql().getPreferenceKey(user)

    def getMoviesRec(pk):
        return db.dbpsql.getMoviesRec(pk)

    def calculatePK(self, cat1, cat2, cat3):
        return round((int(cat1) + int(cat2) + int(cat3)) / 3)

    def getUser(self):
        return db.current_user