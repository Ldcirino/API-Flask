from flask import jsonify, request
from models import db
from models.professor import Professor
from models.turma import Turma

# Classe responsável por controlar as ações relacionadas a turmas
class TurmaController:
    
    @staticmethod
    def listar_turmas():
        """
        Lista todas as turmas cadastradas no Banco de Dados

        Retorna:
            - Se houver registros retorna JSON contendo a lista de turmas e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Turma" usando SQLAlchemy e salva em turmas
        turmas = Turma.query.all()

        # Se houver turmas cadastradas
        if turmas:
            lista = []
            for turma in turmas:
                # Converte para dicionario e adiciona na lista
                lista.append(turma.para_dicionario())
            return jsonify(lista), 200
        # Se não houver turmas cadastradas
        else:
            mensagem = {"Erro": "Lista de Turmas Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_turma(turma_id):  
        """
        Exibe os dados de uma turma específica com base no ID informado

        Parâmetros:
            turma_id (int): ID da turma a ser consultada

        Retorna:
            - Se a turma for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma turma pelo ID usando SQLAlchemy e salva em turma 
        turma = Turma.query.get(turma_id)

        # Se a turma for encontrada
        if turma:
            # Converte para dicionario e retorna como JSON
            return jsonify(turma.para_dicionario()), 200
        # Se a turma não existir no banco de dados
        else:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 404
    
    @staticmethod
    def criar_turma():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        descricao = dados.get("descricao")
        ativo = True if dados.get("ativo") == "True" else False
        professor_id = dados.get("professor_id")

        if (descricao == None or professor_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400

        registro_turma = Turma.query.filter_by(descricao=descricao).first()
        if registro_turma:
            mensagem = {"Erro": "Turma Já Cadastrado!"}
            return jsonify(mensagem), 409
        
        registro_professor = Professor.query.filter_by(id=professor_id).first()
        if not registro_professor:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 422

        nova_turma = Turma(
            descricao = descricao,
            ativo = ativo, 
            professor_id = professor_id
        )

        db.session.add(nova_turma)
        db.session.commit()

        mensagem = {"Mensagem": "Turma Cadastrada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def atualizar_turma(turma_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        turma = Turma.query.get(turma_id)
        if turma is None:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 404
        
        descricao = dados.get("descricao")
        ativo = True if dados.get("ativo") == "True" else False
        professor_id = dados.get("professor_id")

        if (descricao == None or professor_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
      
        registro_professor = Professor.query.filter_by(id=professor_id).first()
        if not registro_professor:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 422

        turma.descricao = descricao
        turma.ativo = ativo
        turma.professor_id = professor_id

        db.session.commit()
        
        mensagem = {"Mensagem": "Turma Atualizada com Sucesso!"}
        return jsonify(mensagem), 200
    
    @staticmethod
    def deletar_turma(turma_id):
        """
        Delete os dados de uma turma específica com base no ID informado

        Parâmetros:
            turma_id (int): ID da turma a ser deletada

        Retorna:
            - Se a turma for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
            - Se existir aluno cadastrado na turma retorna JSON com mensagem de erro e código HTTP 409
        """

        # Busca uma turma pelo ID usando SQLAlchemy e salva em turma
        turma = Turma.query.get(turma_id)

        # Se a turma não for encontrada
        if turma is None:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 404
        
        # Se existir aluno cadastrado na turma
        if turma.alunos:
           return jsonify({"Erro": "Turma com Aluno Vinculado!"}), 409
        
        # Deletar registro no Banco de Dados
        db.session.delete(turma)
        db.session.commit()
        
        mensagem = {"Mensagem": "Turma Deletada com Sucesso!"}
        return jsonify(mensagem), 200