from models import db   # Importa a instância do ORM que acessa o Banco de Dados


# Class que vira uma Tabela no Banco de Dados
class Turma(db.Model):

    # Nome da Tabela
    __tablename__ = 'turmas'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)

    professor_id = db.Column(db.Integer, db.ForeignKey("professores.id"), nullable=False)

    # Relacionamento Muitos-para-Um (N-1) com Tabela Professor
    professor = db.relationship("Professor", back_populates="turmas")

    # Relacionamento Um-para-Muitos (1-N) com Tabela Aluno
    alunos = db.relationship("Aluno", back_populates="turma")

    # Converter atributos da classe em um dicionário para envio em JSON    
    def para_dicionario(self):
        dados = {
            "id": self.id,
            "descricao": self.descricao,
            "ativo": self.ativo, 
            "professor_id": self.professor_id
        }
        return dados    # Retorna dicionário