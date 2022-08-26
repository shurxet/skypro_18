from flask_restx import Namespace, Resource

from app.contaner import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)

director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()

        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)

        return director_schema.dump(director), 200
