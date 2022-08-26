from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all = self.session.query(Director).all()

        return all

    def get_one(self, did):
        one = self.session.query(Director).get(did)

        return one