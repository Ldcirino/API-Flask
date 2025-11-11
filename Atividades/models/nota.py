from models import db   # Importa a instância do ORM que acessa o Banco de Dados


# Class que vira uma Tabela no Banco de Dados
class Nota(db.Model):

    # Nome da Tabela
    __tablename__ = 'notas'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Float, nullable=False)
    aluno_id = db.Column(db.Integer, nullable=False)

    atividade_id = db.Column(db.Integer, db.ForeignKey("atividades.id"), nullable=False)

    # Relacionamento Muitos-para-Um (N-1) com Tabela Atividade
    atividade = db.relationship("Atividade", back_populates="notas")

    # Converter atributos da classe em um dicionario para envio em JSON
    def para_dicionario(self):
        dados = {
            "id": self.id,
            "nota": self.nota,
            "aluno_id": self.aluno_id,
            "atividade_id": self.atividade_id
        }
        return dados # Retorna dicionário