from flask import Blueprint, jsonify, request
from app import db
from app.models import Aluno
from datetime import datetime

bp = Blueprint('alunos', __name__, url_prefix='/api/alunos')

@bp.route('/', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos])

@bp.route('/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    return jsonify(aluno.to_dict())

@bp.route('/', methods=['POST'])
def create_aluno():
    data = request.get_json()
    data_nascimento = None
    if 'data_nascimento' in data and data['data_nascimento']:
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()

    new_aluno = Aluno(
        nome=data['nome'],
        idade=data.get('idade'),
        turma_id=data['turma_id'],
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
        nota_segundo_semestre=data.get('nota_segundo_semestre'),
        media_final=data.get('media_final')
    )
    db.session.add(new_aluno)
    db.session.commit()
    return jsonify(new_aluno.to_dict()), 201

@bp.route('/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    data = request.get_json()
    aluno.nome = data.get('nome', aluno.nome)
    aluno.idade = data.get('idade', aluno.idade)
    aluno.turma_id = data.get('turma_id', aluno.turma_id)
    if 'data_nascimento' in data and data['data_nascimento']:
        aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
    elif 'data_nascimento' in data and data['data_nascimento'] is None:
        aluno.data_nascimento = None
    aluno.nota_primeiro_semestre = data.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
    aluno.nota_segundo_semestre = data.get('nota_segundo_semestre', aluno.nota_segundo_semestre)
    aluno.media_final = data.get('media_final', aluno.media_final)
    db.session.commit()
    return jsonify(aluno.to_dict())

@bp.route('/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno deletado com sucesso'}), 204
