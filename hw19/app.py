from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import ns_user
from views.auth import ns_auth
from views.protected import ns_protected
from dao.model.user import User


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(ns_user)
    api.add_namespace(ns_auth)
    api.add_namespace(ns_protected)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        u3 = User(username="i", password="password", role="admin")
        with db.session.begin():
            db.session.add(u3)


app = create_app(Config())
app.debug = True


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)