from flask import Flask
from database import db
from app.models import Aluno, Professor, Turma
from app.crud_routes import register_crud_routes
from app.extensions import migrate, ma
from flasgger import Swagger
from app.config import DevelopmentConfig

import os

def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Caminho para o banco SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'data.db')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SWAGGER'] = {'title': 'Escolinha Do Barulho', 'uiversion': 3}

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    Swagger(app)

    # Registra rotas CRUD
    register_crud_routes(app)

    # Rota de health check
    @app.route('/api/health')
    def health():
        return {"status": "ok"}
    
    @app.route('/')
    def index():
        return "API Flask rodando! Acesse /apidocs para Swagger."

    
    

    return app

    

app = create_app()

if __name__ == '__main__':
    # Rodar o Flask em 0.0.0.0 para expor no Docker
    app.run(host='0.0.0.0', port=5000, debug=True)
