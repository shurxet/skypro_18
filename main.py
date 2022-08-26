# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from app.config import Config
from app.setup_db import db
from app.views.director import director_ns
from app.views.genre import genre_ns
from app.views.movie import movie_ns


#функция создания основного объекта app
def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)

    return application


#функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    app.run()
