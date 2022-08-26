from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        all = self.dao.get_all()
        return all

    def get_one(self, gid):
        one = self.dao.get_one(gid)
        return one