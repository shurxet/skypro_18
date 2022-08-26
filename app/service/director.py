from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        all = self.dao.get_all()
        return all

    def get_one(self, did):
        one = self.dao.get_one(did)
        return one