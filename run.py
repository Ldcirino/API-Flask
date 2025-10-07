import os
from flask import Flask
from flasgger import Swagger
from database import db
from app.models import Aluno, Professor, Turma
from app.crud_routes import register_crud_routes
from app.extensions import migrate, ma
from app.config import DevelopmentConfig

def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Configuração do banco SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'data.db')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SWAGGER'] = {'title': 'API - Gerenciamento de Alunos', 'uiversion': 3}

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    Swagger(app)

    # Cria as tabelas dentro do app context
    with app.app_context():
        db.create_all()

    # Registra rotas CRUD
    register_crud_routes(app)

    # Rota de health check
    @app.route('/api/health')
    def health():
        return {"status": "ok"}

    # Rota principal
    @app.route('/')
    def index():
        return "API Flask rodando! Acesse /apidocs"

    return app

# Cria app
app = create_app()

if __name__ == '__main__':
    # Rodar Flask
    app.run(host='0.0.0.0', port=5000, debug=True)