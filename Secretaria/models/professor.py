from models import db   # Importa a instância do ORM que acessa o Banco de Dados


# Class que vira uma Tabela no Banco de Dados
class Professor(db.Model):

    # Nome da Tabela
    __tablename__ = 'professores'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    # Relacionamento Um-para-Muitos (1-N) com Tabela Turma
    turmas = db.relationship("Turma", back_populates="professor")
        
    # Converter atributos da classe em um dicionário para envio em JSON
    def para_dicionario(self):
        dados = {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade, 
            "materia": self.materia,
            "observacoes": self.observacoes
        }
        return dados    # Retorna dicionário