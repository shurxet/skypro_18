# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from app.contaner import movie_service


movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)

movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        movies = movie_service.get_all(director_id, genre_id, year)

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)

        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        req_json = request.json
        req_json["mid"] = mid

        movie_service.update(req_json)

        return "", 204

    def patch(self, mid: int):
        req_json = request.json
        req_json["mid"] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)


