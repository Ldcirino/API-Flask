import os   # Biblioteca com funcionalidades do sistema operacional

# Classe para configuração da aplicação Flask
class Config:               
    # Define a URI de conexão com o banco de dados, sendo um SQLite
    # Endereço de conexão indicando que Banco de Dados está no mesmo diretório do projeto
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    # Desativa o rastreamento de modificações de objetos pelo SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Define uma chave secreta, randomicamente, usada pelo Flask para segurança interna
    SECRET_KEY = os.urandom(24)