from models import db   # Importa a instância do ORM que acessa o Banco de Dados


# Class que vira uma Tabela no Banco de Dados
class Aluno(db.Model):

    # Nome da Tabela
    __tablename__ = 'alunos'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)

    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)

    # Relacionamento Muitos-para-Um (N-1) com Tabela Turma
    turma = db.relationship("Turma", back_populates="alunos")
    
    # Converter atributos da classe em um dicionário para envio em JSON
    def para_dicionario(self):
        dados = {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade, 
            "data_nasc": self.data_nasc,
            "turma_id": self.turma_id
        }
        return dados    # Retorna dicionário