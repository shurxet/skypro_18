from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all = self.session.query(Genre).all()

        return all

    def get_one(self, gid):
        one = self.session.query(Genre).get(gid)

        return one