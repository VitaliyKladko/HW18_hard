from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns
from load_data.data import load_test_data


def create_app(config: Config) -> Flask:
    """
    Функция создает приложение, конфигурирует его (из объекта Конфиг), применяет конфигурацию(app.app_context().push())
    и отдает обратно приложение
    """
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def register_extensions(app: Flask):
    """
    Функция подключает расширения к приложению (Flask-SQLAlchemy, Flask-RESTx, ...) и ничего не отдает
    """
    # подключаем БД
    db.init_app(app)
    # привязываем API к приложению
    api = Api(app)
    # добавляем namespace к API
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    application_config = Config()
    application = create_app(application_config)
    register_extensions(application)
    load_test_data()
    application.run(host="localhost", port=10001, debug=True)
