from database import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo
        }