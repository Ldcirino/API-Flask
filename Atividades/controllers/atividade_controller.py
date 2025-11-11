from flask import Blueprint, jsonify, request
import requests
from models import db
from models.atividade import Atividade
from datetime import datetime


# Classe responsável por controlar as ações relacionadas as atividades
class AtividadeController:
    
    # Usando Blueprint para organinar Rotas
    atividade_bp = Blueprint('atividades', __name__)

    @staticmethod
    @atividade_bp.route('/', methods=['GET'])
    def listar_atividades():
        """
        Lista todas as atividades cadastradas no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de atividade e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Atividades" usando SQLAlchemy e salva em atividades
        atividades = Atividade.query.all()

        # Se houver atividades cadastradas
        if atividades:
            lista = []
            for atividade in atividades:
                # Converte para dicionario e adiciona na lista
                lista.append(atividade.para_dicionario())
            return jsonify(lista), 200
        # Se não houver atividades cadastradas
        else:
            mensagem = {"Erro": "Lista de Atividades Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @atividade_bp.route('/<int:atividade_id>', methods=['GET'])
    def exibir_atividade(atividade_id):
        """
        Exibe os dados de uma atividade específica com base no ID informado

        Parâmetros:
            atividade_id (int): ID da atividade a ser consultada

        Retorna:
            - Se a atividade for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma atividade pelo ID usando SQLAlchemy e salva em atividade 
        atividade = Atividade.query.get(atividade_id)

        # Se a atividade for encontrada
        if atividade:
            # Converte para dicionario e retorna como JSON
            return jsonify(atividade.para_dicionario()), 200
        # Se a atividade não existir no banco de dados
        else:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @atividade_bp.route('/', methods=['POST'])
    def criar_atividade():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nome_atividade = dados.get("nome_atividade")
        descricao = dados.get("descricao")
        peso_porcentagem = dados.get("peso_porcentagem")
        data = dados.get("data_entrega")
        turma_id = dados.get("turma_id")
        professor_id = dados.get("professor_id")

        if (nome_atividade == None or descricao == None or peso_porcentagem == None or data == None or turma_id == None or professor_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        
        data_entrega = datetime.strptime(data, "%d/%m/%Y").date()

        registro_atividades = Atividade.query.filter_by(data_entrega=data_entrega)
        if registro_atividades:
            for atividade in registro_atividades:
                if (nome_atividade == atividade.nome_atividade):
                    mensagem = {"Erro": "Atividade dessa Data Já Cadastrada!"}
                    return jsonify(mensagem), 409
        
        # Requisição para SchoolManaganer API para acessar Turmas
        response = requests.get("http://schoolmanager:5000/turmas/{}".format(turma_id))

        if response.status_code != 200:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 404

        # Converter JSON para Objeto
        turma = response.json()
        
        if turma['professor_id'] != professor_id:
            mensagem = {"Erro": "Professor Informado Incorreto!"}
            return jsonify(mensagem), 422

        nova_atividade = Atividade(
            nome_atividade = nome_atividade,
            descricao = descricao, 
            peso_porcentagem = peso_porcentagem,
            data_entrega = data_entrega,
            turma_id = turma_id,
            professor_id = professor_id
        )

        db.session.add(nova_atividade)
        db.session.commit()

        mensagem = {"Mensagem": "Atividade Cadastrada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    @atividade_bp.route('/<int:atividade_id>', methods=['PUT'])
    def atualizar_reserva(atividade_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400
        
        atividade = Atividade.query.get(atividade_id)
        if atividade is None:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 404

        nome_atividade = dados.get("nome_atividade")
        descricao = dados.get("descricao")
        peso_porcentagem = dados.get("peso_porcentagem")
        data = dados.get("data_entrega")
        turma_id = dados.get("turma_id")
        professor_id = dados.get("professor_id")

        if (nome_atividade == None or descricao == None or peso_porcentagem == None or data == None or turma_id == None or professor_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        
        data_entrega = datetime.strptime(data, "%d/%m/%Y").date()

        registro_atividades = Atividade.query.filter_by(data_entrega=data_entrega)
        if registro_atividades:
            for atividade in registro_atividades:
                if (nome_atividade == atividade.nome_atividade):
                    mensagem = {"Erro": "Atividade dessa Data Já Cadastrada!"}
                    return jsonify(mensagem), 409
        
        # Requisição para SchoolManaganer API para acessar Turmas
        response = requests.get("http://schoolmanager:5000/turmas/{}".format(turma_id))

        if response.status_code != 200:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 424

        # Converter JSON para Objeto
        turma = response.json()
        
        if turma['professor_id'] != professor_id:
            mensagem = {"Erro": "Professor Informado Incorreto!"}
            return jsonify(mensagem), 422

        atividade.nome_atividade = nome_atividade
        atividade.descricao = descricao
        atividade.peso_porcentagem = peso_porcentagem
        atividade.data_entrega = data_entrega,
        atividade.turma_id = turma_id,
        atividade.professor_id = professor_id

        db.session.commit()

        mensagem = {"Mensagem": "Atividade Atualizada com Sucesso!"}
        return jsonify(mensagem), 200
        
    @staticmethod
    @atividade_bp.route('/<int:atividade_id>', methods=['DELETE'])
    def deletar_atividade(atividade_id):
        """
        Delete os atividade de uma nota específica com base no ID informado

        Parâmetros:
            atividade_id (int): ID da atividade a ser deletada

        Retorna:
            - Se a atividade for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
            - Se existir nota vinculada a atividade retorna JSON com mensagem de erro e código HTTP 409
        """

        # Busca uma atividade pelo ID usando SQLAlchemy e salva em atividade
        atividade = Atividade.query.get(atividade_id)

        # Se a atividade não for encontrada
        if atividade is None:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 404
        
        # Se existir nota vinculada a atividade
        if atividade.notas:
           return jsonify({"Erro": "Atividade com Nota Vinculado!"}), 409
            
        # Deletar registro no Banco de Dados
        db.session.delete(atividade)
        db.session.commit()
            
        mensagem = {"Mensagem": "Atividade Deletada com Sucesso!"}
        return jsonify(mensagem), 200