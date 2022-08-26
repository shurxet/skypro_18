# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, director_id, genre_id, year):
        all = self.dao.get_all()

        if genre_id:
            all = self.dao.get_by_genre(genre_id)
        if director_id:
            all = self.dao.get_by_director(director_id)
        if year:
            all = self.dao.get_by_year(year)
        return all

    def get_one(self, mid):
        one = self.dao.get_one(mid)
        return one

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        result = self.get_one(mid)

        result.title = data.get("title")
        result.description = data.get("description")
        result.trailer = data.get("trailer")
        result.year = data.get("year")
        result.rating = data.get("rating")

        self.dao.update(result)

        return result

    def update_partial(self, data):
        mid = data.get("id")
        result = self.get_one(mid)

        if "title" in data:
            result.title = data.get("title")
        if "description" in data:
            result.description = data.get("description")
        if "trailer" in data:
            result.trailer = data.get("trailer")
        if "year" in data:
            result.year = data.get("year")
        if "rating" in data:
            result.rating = data.get("rating")

        self.dao.update(result)

        return result

    def delete(self, mid):
        self.dao.delete(mid)




