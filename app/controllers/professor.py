from flask import Blueprint, jsonify, request
from app import db
from app.models import Professor

bp = Blueprint('professores', __name__, url_prefix='/api/professores')

@bp.route('/', methods=['GET'])
def get_professores():
    professores = Professor.query.all()
    return jsonify([p.to_dict() for p in professores])

@bp.route('/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)
    return jsonify(professor.to_dict())

@bp.route('/', methods=['POST'])
def create_professor():
    data = request.get_json()
    new_professor = Professor(
        nome=data['nome'],
        idade=data.get('idade'),
        materia=data.get('materia'),
        observacoes=data.get('observacoes')
    )
    db.session.add(new_professor)
    db.session.commit()
    return jsonify(new_professor.to_dict()), 201

@bp.route('/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)
    data = request.get_json()
    professor.nome = data.get('nome', professor.nome)
    professor.idade = data.get('idade', professor.idade)
    professor.materia = data.get('materia', professor.materia)
    professor.observacoes = data.get('observacoes', professor.observacoes)
    db.session.commit()
    return jsonify(professor.to_dict())

@bp.route('/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message': 'Professor deletado com sucesso'}), 204
