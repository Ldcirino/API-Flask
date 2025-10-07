from flask import request, jsonify
from sqlalchemy import inspect, text
from flasgger import swag_from
from database import db
from app.models import Aluno, Professor, Turma

def register_crud_routes(app):

    # ------------------- ALUNO -------------------
    @app.route('/aluno', methods=['POST'])
    @swag_from({
        'tags': ['Aluno'],
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {'nome': {'type': 'string'}, 'idade': {'type': 'integer'}},
                'required': ['nome', 'idade']
            }
        }],
        'responses': {201: {'description': 'Aluno criado'}}
    })
    def create_aluno():
        data = request.get_json()
        aluno_novo = Aluno(nome=data.get('nome'), idade=data.get('idade'))
        db.session.add(aluno_novo)
        db.session.commit()
        return jsonify({"message": "Aluno criado", "id": aluno_novo.id}), 201

    @app.route('/aluno', methods=['GET'])
    @swag_from({
        'tags': ['Aluno'],
        'responses': {200: {'description': 'Lista de alunos'}}
    })
    def get_alunos():
        alunos = Aluno.query.all()
        return jsonify([{"id": a.id, "nome": a.nome, "idade": a.idade} for a in alunos])

    @app.route('/aluno/<int:aluno_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Aluno'],
        'parameters': [
            {'name': 'aluno_id', 'in': 'path', 'type': 'integer', 'required': True},
            {'name': 'body', 'in': 'body', 'schema': {
                'type': 'object',
                'properties': {'nome': {'type': 'string'}, 'idade': {'type': 'integer'}}
            }}
        ],
        'responses': {200: {'description': 'Aluno atualizado'}}
    })
    def update_aluno(aluno_id):
        data = request.get_json()
        aluno_obj = Aluno.query.get_or_404(aluno_id)
        aluno_obj.nome = data.get('nome', aluno_obj.nome)
        aluno_obj.idade = data.get('idade', aluno_obj.idade)
        db.session.commit()
        return jsonify({"message": "Aluno atualizado"})

    @app.route('/aluno/<int:aluno_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Aluno'],
        'parameters': [{'name': 'aluno_id', 'in': 'path', 'type': 'integer', 'required': True}],
        'responses': {200: {'description': 'Aluno deletado'}}
    })
    def delete_aluno(aluno_id):
        aluno_obj = Aluno.query.get_or_404(aluno_id)
        db.session.delete(aluno_obj)
        db.session.commit()
        return jsonify({"message": "Aluno deletado"})


    # ------------------- PROFESSOR -------------------
    @app.route('/professor', methods=['POST'])
    @swag_from({
        'tags': ['Professor'],
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {'nome': {'type': 'string'}, 'disciplina': {'type': 'string'}},
                'required': ['nome', 'disciplina']
            }
        }],
        'responses': {201: {'description': 'Professor criado'}}
    })
    def create_professor():
        data = request.get_json()
        prof_novo = Professor(nome=data.get('nome'), disciplina=data.get('disciplina'))
        db.session.add(prof_novo)
        db.session.commit()
        return jsonify({"message": "Professor criado", "id": prof_novo.id}), 201

    @app.route('/professor', methods=['GET'])
    @swag_from({
        'tags': ['Professor'],
        'responses': {200: {'description': 'Lista de professores'}}
    })
    def get_professores():
        professores = Professor.query.all()
        return jsonify([{"id": p.id, "nome": p.nome, "disciplina": p.disciplina} for p in professores])

    @app.route('/professor/<int:prof_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Professor'],
        'parameters': [
            {'name': 'prof_id', 'in': 'path', 'type': 'integer', 'required': True},
            {'name': 'body', 'in': 'body', 'schema': {
                'type': 'object',
                'properties': {'nome': {'type': 'string'}, 'disciplina': {'type': 'string'}}
            }}
        ],
        'responses': {200: {'description': 'Professor atualizado'}}
    })
    def update_professor(prof_id):
        data = request.get_json()
        prof_obj = Professor.query.get_or_404(prof_id)
        prof_obj.nome = data.get('nome', prof_obj.nome)
        prof_obj.disciplina = data.get('disciplina', prof_obj.disciplina)
        db.session.commit()
        return jsonify({"message": "Professor atualizado"})

    @app.route('/professor/<int:prof_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Professor'],
        'parameters': [{'name': 'prof_id', 'in': 'path', 'type': 'integer', 'required': True}],
        'responses': {200: {'description': 'Professor deletado'}}
    })
    def delete_professor(prof_id):
        prof_obj = Professor.query.get_or_404(prof_id)
        db.session.delete(prof_obj)
        db.session.commit()
        return jsonify({"message": "Professor deletado"})


    # ------------------- TURMA -------------------
    @app.route('/turma', methods=['POST'])
    @swag_from({
        'tags': ['Turma'],
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {'nome': {'type': 'string'}, 'professor_id': {'type': 'integer'}},
                'required': ['nome', 'professor_id']
            }
        }],
        'responses': {201: {'description': 'Turma criada'}}
    })
    def create_turma():
        data = request.get_json()
        turma_nova = Turma(nome=data.get('nome'), professor_id=data.get('professor_id'))
        db.session.add(turma_nova)
        db.session.commit()
        return jsonify({"message": "Turma criada", "id": turma_nova.id}), 201

    @app.route('/turma', methods=['GET'])
    @swag_from({
        'tags': ['Turma'],
        'responses': {200: {'description': 'Lista de turmas'}}
    })
    def get_turmas():
        turmas = Turma.query.all()
        return jsonify([{"id": t.id, "nome": t.nome, "professor_id": t.professor_id} for t in turmas])

    @app.route('/turma/<int:turma_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Turma'],
        'parameters': [
            {'name': 'turma_id', 'in': 'path', 'type': 'integer', 'required': True},
            {'name': 'body', 'in': 'body', 'schema': {
                'type': 'object',
                'properties': {'nome': {'type': 'string'}, 'professor_id': {'type': 'integer'}}
            }}
        ],
        'responses': {200: {'description': 'Turma atualizada'}}
    })
    def update_turma(turma_id):
        data = request.get_json()
        turma_obj = Turma.query.get_or_404(turma_id)
        turma_obj.nome = data.get('nome', turma_obj.nome)
        turma_obj.professor_id = data.get('professor_id', turma_obj.professor_id)
        db.session.commit()
        return jsonify({"message": "Turma atualizada"})

    @app.route('/turma/<int:turma_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Turma'],
        'parameters': [{'name': 'turma_id', 'in': 'path', 'type': 'integer', 'required': True}],
        'responses': {200: {'description': 'Turma deletada'}}
    })
    def delete_turma(turma_id):
        turma_obj = Turma.query.get_or_404(turma_id)
        db.session.delete(turma_obj)
        db.session.commit()
        return jsonify({"message": "Turma deletada"})


    # ------------------- SHOW DB -------------------
    @app.route('/show-db', methods=['GET'])
    @swag_from({
        'tags': ['Banco'],
        'responses': {200: {'description': 'Mostra todo o banco'}}
    })
    def show_db():
        try:
            inspector = inspect(db.engine)
            all_data = {}
            for table_name in inspector.get_table_names():
                result = db.session.execute(text(f'SELECT * FROM {table_name}')).fetchall()
                columns = inspector.get_columns(table_name)
                col_names = [col['name'] for col in columns]

                table_data = []
                for row in result:
                    table_data.append({col_names[i]: row[i] for i in range(len(col_names))})

                all_data[table_name] = table_data

            return jsonify(all_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
