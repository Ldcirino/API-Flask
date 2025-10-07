from app import create_app
from database import db
from app import models  # garante que Professor, Turma, Aluno sejam carregados

# cria a aplicação usando a factory
app = create_app()

def reset_database():
    with app.app_context():
        print(">> Apagando todas as tabelas...")
        db.drop_all()
        print(">> Recriando todas as tabelas...")
        db.create_all()
        print(">> Banco de dados resetado com sucesso!")

if __name__ == "__main__":
    reset_database()