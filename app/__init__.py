
from flask import Flask
from database import db
from app.extensions import migrate, ma
from app.routes import register_routes
from flasgger import Swagger
from app.config import DevelopmentConfig  # 👈 aqui
from app.models import aluno, professor, turma  # garante migrações

import os

def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    basedir = os.path.abspath(os.path.dirname(__file__) + '/../')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{basedir}/data.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SWAGGER'] = {'title': 'School API', 'uiversion': 3}

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    Swagger(app)

    return app
