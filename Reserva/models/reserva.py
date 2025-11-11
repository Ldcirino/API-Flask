from models import db   # Importa a instância do ORM que acessa o Banco de Dados


# Class que vira uma Tabela no Banco de Dados
class Reserva(db.Model):

    # Nome da Tabela
    __tablename__ = 'reservas'

    # Colunas da Tabela
    id = db.Column(db.Integer, primary_key = True)
    num_sala = db.Column(db.Integer, nullable=False)
    lab = db.Column(db.Boolean, nullable=False)
    data = db.Column(db.Date, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)

    # Converter atributos da classe em um dicionario para envio em JSON
    def para_dicionario(self):
        dados = {
            "id": self.id,
            "num_sala": self.num_sala,
            "lab": self.lab,
            "data": self.data,
            "turma_id": self.turma_id
        }
        return dados # Retorna dicionário