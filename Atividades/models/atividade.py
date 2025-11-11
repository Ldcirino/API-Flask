from models import db   # Importa a instância do ORM que acessa o Banco de Dados


# Class que vira uma Tabela no Banco de Dados
class Atividade(db.Model):

    # Nome da Tabela
    __tablename__ = 'atividades'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key = True)
    nome_atividade = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    peso_porcentagem = db.Column(db.Integer, nullable=False)
    data_entrega = db.Column(db.Date, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)

    # Relacionamento Um-para-Muitos (1-N) com Tabela Nota
    notas = db.relationship("Nota", back_populates="atividade")

    # Converter atributos da classe em um dicionario para envio em JSON
    def para_dicionario(self):
        dados = {
            "id": self.id,
            "nome_atividade": self.nome_atividade,
            "descricao": self.descricao,
            "peso_porcentagem": self.peso_porcentagem,
            "data_entrega": self.data_entrega,
            "turma_id": self.turma_id,
            "professor_id": self.professor_id
        }
        return dados # Retorna dicionário