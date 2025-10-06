import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuração padrão da aplicação Flask"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(basedir, '..', 'data.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret"

    SWAGGER = {
        "title": "School API",
        "uiversion": 3,
        "openapi": "3.0.2",
        "description": "API RESTful para gerenciar Professores, Turmas e Alunos."
    }

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
