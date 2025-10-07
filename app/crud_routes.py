from flask import request, jsonify
from sqlalchemy import inspect, text
from flasgger import swag_from
from database import db
from app.models import Aluno, Professor, Turma
from datetime import datetime


def register_crud_routes(app):

    # ------------------- ALUNO -------------------
    @app.route('/aluno', methods=['POST'])
    @swag_from({
        'tags': ['Aluno'],
        'summary': 'Cria um novo aluno',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'turma_id': {'type': 'integer'},
                    'data_nascimento': {'type': 'string', 'format': 'date'},
                    'semestre': {'type': 'string'},
                    'nota_semestre': {'type': 'number'},
                    'media_final': {'type': 'number'}
                },
                'required': ['nome', 'idade', 'turma_id', 'data_nascimento']
            }
        }],
        'responses': {201: {'description': 'Aluno criado com sucesso'}}
    })
    def create_aluno():
        data = request.get_json()
        try:
            data_nasc = datetime.strptime(data.get('data_nascimento'), '%Y-%m-%d').date()
        except Exception:
            return jsonify({"error": "data_nascimento inválida. Use o formato YYYY-MM-DD"}), 400

        aluno_novo = Aluno(
            nome=data.get('nome'),
            idade=data.get('idade'),
            turma_id=data.get('turma_id'),
            data_nascimento=data_nasc,
            semestre=data.get('semestre'),
            nota_semestre=data.get('nota_semestre'),
            media_final=data.get('media_final')
        )

        db.session.add(aluno_novo)
        db.session.commit()
        return jsonify({"message": "Aluno criado", "id": aluno_novo.id}), 201

    @app.route('/aluno', methods=['GET'])
    @swag_from({
        'tags': ['Aluno'],
        'summary': 'Lista todos os alunos',
        'responses': {200: {'description': 'Lista de alunos'}}
    })
    def get_alunos():
        alunos = Aluno.query.all()
        return jsonify([a.to_dict() for a in alunos])

    @app.route('/aluno/<int:aluno_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Aluno'],
        'summary': 'Atualiza um aluno existente',
        'parameters': [
            {'name': 'aluno_id', 'in': 'path', 'type': 'integer', 'required': True},
            {'name': 'body', 'in': 'body', 'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'turma_id': {'type': 'integer'},
                    'data_nascimento': {'type': 'string', 'format': 'date'},
                    'semestre': {'type': 'string'},
                    'nota_semestre': {'type': 'number'},
                    'media_final': {'type': 'number'}
                }
            }}
        ],
        'responses': {200: {'description': 'Aluno atualizado com sucesso'}}
    })
    def update_aluno(aluno_id):
        data = request.get_json()
        aluno = Aluno.query.get_or_404(aluno_id)

        if 'data_nascimento' in data:
            try:
                aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
            except Exception:
                return jsonify({"error": "data_nascimento inválida. Use o formato YYYY-MM-DD"}), 400

        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        aluno.turma_id = data.get('turma_id', aluno.turma_id)
        aluno.semestre = data.get('semestre', aluno.semestre)
        aluno.nota_semestre = data.get('nota_semestre', aluno.nota_semestre)
        aluno.media_final = data.get('media_final', aluno.media_final)

        db.session.commit()
        return jsonify({"message": "Aluno atualizado"})

    @app.route('/aluno/<int:aluno_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Aluno'],
        'summary': 'Deleta um aluno',
        'parameters': [{'name': 'aluno_id', 'in': 'path', 'type': 'integer', 'required': True}],
        'responses': {200: {'description': 'Aluno deletado com sucesso'}}
    })
    def delete_aluno(aluno_id):
        aluno = Aluno.query.get_or_404(aluno_id)
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({"message": "Aluno deletado"})


    # ------------------- PROFESSOR -------------------
    @app.route('/professor', methods=['POST'])
    @swag_from({
        'tags': ['Professor'],
        'summary': 'Cria um novo professor',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'materia': {'type': 'string'},
                    'observacoes': {'type': 'string'}
                },
                'required': ['nome', 'idade', 'materia']
            }
        }],
        'responses': {201: {'description': 'Professor criado com sucesso'}}
    })
    def create_professor():
        data = request.get_json()
        prof_novo = Professor(
            nome=data.get('nome'),
            idade=data.get('idade'),
            materia=data.get('materia'),
            observacoes=data.get('observacoes')
        )
        db.session.add(prof_novo)
        db.session.commit()
        return jsonify({"message": "Professor criado", "id": prof_novo.id}), 201

    @app.route('/professor', methods=['GET'])
    @swag_from({
        'tags': ['Professor'],
        'summary': 'Lista todos os professores',
        'responses': {200: {'description': 'Lista de professores'}}
    })
    def get_professores():
        professores = Professor.query.all()
        return jsonify([p.to_dict() for p in professores])

    @app.route('/professor/<int:prof_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Professor'],
        'summary': 'Atualiza um professor existente',
        'parameters': [
            {'name': 'prof_id', 'in': 'path', 'type': 'integer', 'required': True},
            {'name': 'body', 'in': 'body', 'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'materia': {'type': 'string'},
                }
            }}
        ],
        'responses': {200: {'description': 'Professor atualizado com sucesso'}}
    })
    def update_professor(prof_id):
        data = request.get_json()
        prof = Professor.query.get_or_404(prof_id)
        prof.nome = data.get('nome', prof.nome)
        prof.idade = data.get('idade', prof.idade)
        prof.materia = data.get('materia', prof.materia)
        prof.observacoes = data.get('observacoes', prof.observacoes)
        db.session.commit()
        return jsonify({"message": "Professor atualizado"})

    @app.route('/professor/<int:prof_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Professor'],
        'summary': 'Deleta um professor',
        'parameters': [{'name': 'prof_id', 'in': 'path', 'type': 'integer', 'required': True}],
        'responses': {200: {'description': 'Professor deletado com sucesso'}}
    })
    def delete_professor(prof_id):
        prof = Professor.query.get_or_404(prof_id)
        db.session.delete(prof)
        db.session.commit()
        return jsonify({"message": "Professor deletado"})


    # ------------------- TURMA -------------------
    @app.route('/turma', methods=['POST'])
    @swag_from({
        'tags': ['Turma'],
        'summary': 'Cria uma nova turma',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'descricao': {'type': 'string'},
                    'professor_id': {'type': 'integer'},
                    'ativo': {'type': 'boolean'}
                },
                'required': ['descricao', 'professor_id']
            }
        }],
        'responses': {201: {'description': 'Turma criada com sucesso'}}
    })
    def create_turma():
        data = request.get_json()
        turma_nova = Turma(
            descricao=data.get('descricao'),
            professor_id=data.get('professor_id'),
            ativo=data.get('ativo', True)
        )
        db.session.add(turma_nova)
        db.session.commit()
        return jsonify({"message": "Turma criada", "id": turma_nova.id}), 201

    @app.route('/turma', methods=['GET'])
    @swag_from({
        'tags': ['Turma'],
        'summary': 'Lista todas as turmas',
        'responses': {200: {'description': 'Lista de turmas'}}
    })
    def get_turmas():
        turmas = Turma.query.all()
        return jsonify([t.to_dict() for t in turmas])

    @app.route('/turma/<int:turma_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Turma'],
        'summary': 'Atualiza uma turma existente',
        'parameters': [
            {'name': 'turma_id', 'in': 'path', 'type': 'integer', 'required': True},
            {'name': 'body', 'in': 'body', 'schema': {
                'type': 'object',
                'properties': {
                    'descricao': {'type': 'string'},
                    'professor_id': {'type': 'integer'},
                    'ativo': {'type': 'boolean'}
                }
            }}
        ],
        'responses': {200: {'description': 'Turma atualizada com sucesso'}}
    })
    def update_turma(turma_id):
        data = request.get_json()
        turma = Turma.query.get_or_404(turma_id)
        turma.descricao = data.get('descricao', turma.descricao)
        turma.professor_id = data.get('professor_id', turma.professor_id)
        turma.ativo = data.get('ativo', turma.ativo)
        db.session.commit()
        return jsonify({"message": "Turma atualizada"})

    @app.route('/turma/<int:turma_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Turma'],
        'summary': 'Deleta uma turma',
        'parameters': [{'name': 'turma_id', 'in': 'path', 'type': 'integer', 'required': True}],
        'responses': {200: {'description': 'Turma deletada com sucesso'}}
    })
    def delete_turma(turma_id):
        turma = Turma.query.get_or_404(turma_id)
        db.session.delete(turma)
        db.session.commit()
        return jsonify({"message": "Turma deletada"})


    # ------------------- SHOW DB -------------------
    @app.route('/show-db', methods=['GET'])
    @swag_from({
        'tags': ['Banco'],
        'summary': 'Exibe todos os dados do banco',
        'responses': {200: {'description': 'Conteúdo completo das tabelas'}}
    })
    def show_db():
        try:
            inspector = inspect(db.engine)
            all_data = {}
            for table_name in inspector.get_table_names():
                result = db.session.execute(text(f'SELECT * FROM {table_name}')).fetchall()
                columns = inspector.get_columns(table_name)
                col_names = [col['name'] for col in columns]
                table_data = [{col_names[i]: row[i] for i in range(len(col_names))} for row in result]
                all_data[table_name] = table_data
            return jsonify(all_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
