from flask import Flask         # Para importar a classe principal Flask
from flasgger import Swagger    # Para gerar a documentação da API
from config import Config
from models import db
from controllers.atividade_controller import AtividadeController
from controllers.nota_controller import NotaController


# Cria a instância principal da aplicação Flask
app = Flask(__name__)

# Carrega as configurações definidas na classe Config
app.config.from_object(Config)

# Inicializa o Swagger para gerar a documentação da API com base no arquivo swagger.yml
swagger = Swagger(app, template_file='swagger.yml')

# Inicializa o SQLAlchemy, conectando o ORM à aplicação Flask
db.init_app(app)

# Cria Tabelas do Banco de Dados
with app.app_context():
    db.create_all()

# Rotas via Blueprint
app.register_blueprint(AtividadeController.atividade_bp, url_prefix='/atividades')
app.register_blueprint(NotaController.notas_bp, url_prefix='/notas')

# Executar código quando o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=False, port=5001)  # Definindo porta 5001 para rodar API