from flask import jsonify, request
from models import db
from models.aluno import Aluno
from models.turma import Turma
from datetime import datetime

# Classe responsável por controlar as ações relacionadas aos alunos
class AlunoController:
    
    @staticmethod
    def listar_alunos():
        """
        Lista todos os alunos cadastrados no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de alunos e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Aluno" usando SQLAlchemy e salva em alunos
        alunos = Aluno.query.all()

        # Se houver alunos cadastrados
        if alunos:
            lista = []
            for aluno in alunos:
                # Converte para dicionario e adiciona na lista
                lista.append(aluno.para_dicionario())
            return jsonify(lista), 200
        # Se não houver alunos cadastrados
        else:
            mensagem = {"Erro": "Lista de Alunos Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_aluno(aluno_id):
        """
        Exibe os dados de um aluno específico com base no ID informado

        Parâmetros:
            aluno_id (int): ID do aluno a ser consultado

        Retorna:
            - Se o aluno for encontrado retorna JSON com seus dados e código HTTP 200
            - Se não for encontrado retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca um aluno pelo ID usando SQLAlchemy e salva em aluno 
        aluno = Aluno.query.get(aluno_id)

        # Se o aluno for encontrado
        if aluno:
            # Converte para dicionario e retorna como JSON
            return jsonify(aluno.para_dicionario()), 200
        # Se o aluno não existir no banco de dados
        else:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404
    
    @staticmethod
    def criar_aluno():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nome = dados.get("nome")
        idade = dados.get("idade")
        data = dados.get("data_nasc")
        turma_id = dados.get("turma_id")

        if (nome == None or idade == None or data == None or turma_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        data_nasc = datetime.strptime(data, "%d/%m/%Y").date()

        registro_alunos = Aluno.query.filter_by(nome=nome).first()
        if registro_alunos:
            mensagem = {"Erro": "Aluno Já Cadastrado!"}
            return jsonify(mensagem), 409
        
        registro_turmas = Turma.query.filter_by(id=turma_id).first()
        if not registro_turmas:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 422

        novo_aluno = Aluno(
            nome = nome,
            idade = idade, 
            data_nasc = data_nasc,
            turma_id = turma_id
        )

        db.session.add(novo_aluno)
        db.session.commit()

        mensagem = {"Mensagem": "Aluno Cadastrado com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def atualizar_aluno(aluno_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        aluno = Aluno.query.get(aluno_id)
        if aluno is None:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        nome = dados.get("nome")
        idade = dados.get("idade")
        data = dados.get("data_nasc")
        turma_id = dados.get("turma_id")

        if (nome == None or idade == None or data == None or turma_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        data_nasc = datetime.strptime(data, "%d/%m/%Y").date()
      
        registro_turmas = Turma.query.filter_by(id=turma_id).first()
        if not registro_turmas:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 422

        aluno.nome = nome
        aluno.idade = idade 
        aluno.data_nasc = data_nasc
        aluno.turma_id = turma_id

        db.session.commit()
        
        mensagem = {"Mensagem": "Aluno Atualizado com Sucesso!"}
        return jsonify(mensagem), 200
    
    @staticmethod
    def deletar_aluno(aluno_id):
        """
        Delete os dados de um aluno específico com base no ID informado

        Parâmetros:
            aluno_id (int): ID do aluno a ser deletado

        Retorna:
            - Se o aluno for encontrado retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrado retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca um aluno pelo ID usando SQLAlchemy e salva em aluno
        aluno = Aluno.query.get(aluno_id)

        # Se o aluno não for encontrado
        if aluno is None:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        # Deletar registro no Banco de Dados
        db.session.delete(aluno)
        db.session.commit()
        
        mensagem = {"Mensagem": "Aluno Deletado com Sucesso!"}
        return jsonify(mensagem), 200