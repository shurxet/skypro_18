# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from app.contaner import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)

genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()

        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)

        return genre_schema.dump(genre), 200


