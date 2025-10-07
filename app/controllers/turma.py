from flask import Blueprint, jsonify, request
from app import db
from app.models import Turma

bp = Blueprint('turmas', __name__, url_prefix='/api/turmas')

@bp.route('/', methods=['GET'])
def get_turmas():
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas])

@bp.route('/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    turma = Turma.query.get_or_404(turma_id)
    return jsonify(turma.to_dict())

@bp.route('/', methods=['POST'])
def create_turma():
    data = request.get_json()
    new_turma = Turma(
        descricao=data['descricao'],
        professor_id=data['professor_id'],
        ativo=data.get('ativo', True)
    )
    db.session.add(new_turma)
    db.session.commit()
    return jsonify(new_turma.to_dict()), 201

@bp.route('/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    turma = Turma.query.get_or_404(turma_id)
    data = request.get_json()
    turma.descricao = data.get('descricao', turma.descricao)
    turma.professor_id = data.get('professor_id', turma.professor_id)
    turma.ativo = data.get('ativo', turma.ativo)
    db.session.commit()
    return jsonify(turma.to_dict())

@bp.route('/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    turma = Turma.query.get_or_404(turma_id)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'message': 'Turma deletada com sucesso'}), 204
