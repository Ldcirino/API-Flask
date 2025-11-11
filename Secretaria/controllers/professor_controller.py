from flask import jsonify, request
from models import db
from models.professor import Professor

# Classe responsável por controlar as ações relacionadas aos professores
class ProfessorController:
    
    @staticmethod
    def listar_professores():
        """
        Lista todos os professores cadastrados no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de professores e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Professor" usando SQLAlchemy e salva em professores
        professores = Professor.query.all()

        # Se houver professores cadastrados
        if professores:
            lista = []
            for professor in professores:
                # Converte para dicionario e adiciona na lista
                lista.append(professor.para_dicionario())
            return jsonify(lista), 200
        # Se não houver professores cadastrados
        else:
            mensagem = {"Erro": "Lista de Professores Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_professor(professor_id):
        """
        Exibe os dados de um professor específico com base no ID informado

        Parâmetros:
            professor_id (int): ID do professor a ser consultado

        Retorna:
            - Se o professor for encontrado retorna JSON com seus dados e código HTTP 200
            - Se não for encontrado retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca um professor pelo ID usando SQLAlchemy e salva em professor 
        professor = Professor.query.get(professor_id)

        # Se o professor for encontrado
        if professor:
            # Converte para dicionario e retorna como JSON
            return jsonify(professor.para_dicionario()), 200
        # Se o professor não existir no banco de dados
        else:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 404
    
    @staticmethod
    def criar_professor():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nome = dados.get("nome")
        idade = dados.get("idade")
        materia = dados.get("materia")
        observacoes = dados.get("observacoes")

        if (nome == None or idade == None or materia == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400

        registro_professor = Professor.query.filter_by(nome=nome).first()
        if registro_professor:
            mensagem = {"Erro": "Professor Já Cadastrado!"}
            return jsonify(mensagem), 409

        novo_professor = Professor(
            nome = nome,
            idade = idade, 
            materia = materia,
            observacoes = observacoes
        )

        db.session.add(novo_professor)
        db.session.commit()

        mensagem = {"Mensagem": "Professor Cadastrado com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    def atualizar_professor(professor_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        professor = Professor.query.get(professor_id)
        if professor is None:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        nome = dados.get("nome")
        idade = dados.get("idade")
        materia = dados.get("materia")
        observacoes = dados.get("observacoes")

        if (nome == None or idade == None or materia == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
      
        professor.nome = nome
        professor.idade = idade 
        professor.materia = materia
        professor.observacoes = observacoes

        db.session.commit()
        
        mensagem = {"Mensagem": "Professor Atualizado com Sucesso!"}
        return jsonify(mensagem), 200
    
    @staticmethod
    def deletar_professor(professor_id):
        """
        Delete os dados de um professor específico com base no ID informado

        Parâmetros:
            professor_id (int): ID do professor a ser deletado

        Retorna:
            - Se o professor for encontrado retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrado retorna JSON com mensagem de erro e código HTTP 404
            - Se existir turma vinculada ao professor retorna JSON com mensagem de erro e código HTTP 409
        """

        # Busca um professor pelo ID usando SQLAlchemy e salva em professor
        professor = Professor.query.get(professor_id)

        # Se o professor não for encontrado
        if professor is None:
            mensagem = {"Erro": "Professor Não Cadastrado!"}
            return jsonify(mensagem), 404
        
        # Se existir turma vinculada ao professor
        if professor.turmas:
            return jsonify({"Erro": "Professor com Turma Vinculada!"}), 409
        
        # Deletar registro no Banco de Dados
        db.session.delete(professor)
        db.session.commit()
        
        mensagem = {"Mensagem": "Professor Deletado com Sucesso!"}
        return jsonify(mensagem), 200