from database import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    semestre = db.Column(db.String(50))
    nota_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento.isoformat() if self.data_nascimento else None,
            'semestre': self.semestre,
            'nota_primeiro_semestre': self.nota_semestre,
            'media_final': self.media_final
        }