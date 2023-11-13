class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def getId(self):
        return self._id
    

class Movie:
    def __init__(self, id, title):
        self._id = id
        self._title = title

    def getId(self):
        return self._id

    def getTitle(self):
        return self._title