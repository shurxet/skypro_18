# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return  self.session.query(Movie).all()

    def get_by_genre(self, data):
        return self.session.query(Movie).filter(Movie.genre_id == data)

    def get_by_director(self, data):
        return self.session.query(Movie).filter(Movie.director_id == data)

    def get_by_year(self, data):
        return self.session.query(Movie).filter(Movie.year == data)

    def get_one(self, mid):
        one = self.session.query(Movie).get(mid)

        return one

    def create(self, data):
        new = Movie(**data)

        self.session.add(new)
        self.session.commit()

        return new

    def update(self, data):
        self.session.add(data)
        self.session.commit()

        return data

    def delete(self, mid):
        one = self.get_one(mid)
        self.session.delete(one)
        self.session.commit()

