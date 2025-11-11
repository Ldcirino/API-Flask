from flask import Flask         # Para importar a classe principal Flask
from flasgger import Swagger    # Para gerar a documentação da API
from config import Config
from models import db
from controllers.reserva_controller import ReservaController


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
app.register_blueprint(ReservaController.reservas_bp, url_prefix='/reservas')

# Executar código quando o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=False, port=5002)  # Definindo porta 5002 para rodar API