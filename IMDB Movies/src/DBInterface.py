from abc import ABC, abstractmethod

class DBInterface(ABC):

    @abstractmethod
    def getPassword(self, email):
        """Get user password given email"""
        pass

    @abstractmethod
    def getPreferenceKey(self, user_id):
        """Get user preference key given user id"""
        pass
        
    @abstractmethod
    def getOrderedSetting(self, user_id):
        """Returns if user has the setting ordered by descending rating"""
        pass

    @abstractmethod
    def registerUser(self, email, password):
        """Register new user"""
        pass

    @abstractmethod
    def savePreferences(self, user_id, preference_key, ordered):
        """Save user preferences"""
        pass

    @abstractmethod
    def getMoviesRec(self, pk, ordered):
        """Get user recommended movies given preference key and if its descending or ascending """
        pass 

    @abstractmethod    
    def isMoviesTableEmpty():
        """Gets if the movies table is empty or not"""
        pass