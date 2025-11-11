from flask import Blueprint, jsonify, request
import requests
from models import db
from models.reserva import Reserva
from datetime import datetime


# Classe responsável por controlar as ações relacionadas as reservas
class ReservaController:

    # Usando Blueprint para organinar Rotas
    reservas_bp = Blueprint('reservas', __name__)
    
    @staticmethod
    @reservas_bp.route('/', methods=['GET'])
    def listar_reservas():
        """
        Lista todas as reservas cadastradas no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de reservas e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Reserva" usando SQLAlchemy e salva em reservas
        reservas = Reserva.query.all()

        # Se houver reservas cadastradas
        if reservas:
            lista = []
            for reserva in reservas:
                # Converte para dicionario e adiciona na lista
                lista.append(reserva.para_dicionario())
            return jsonify(lista), 200
        # Se não houver reservas cadastradas
        else:
            mensagem = {"Erro": "Lista de Reservas Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @reservas_bp.route('/<int:reserva_id>', methods=['GET'])
    def exibir_reserva(reserva_id):
        """
        Exibe os dados de uma reserva específica com base no ID informado

        Parâmetros:
            reserva_id (int): ID da reserva a ser consultada

        Retorna:
            - Se a reserva for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma reserva pelo ID usando SQLAlchemy e salva em reserva 
        reserva = Reserva.query.get(reserva_id)

        # Se a reserva for encontrada
        if reserva:
            # Converte para dicionario e retorna como JSON
            return jsonify(reserva.para_dicionario()), 200
        # Se a reserva não existir no banco de dados
        else:
            mensagem = {"Erro": "Reserva Não Cadastrada!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @reservas_bp.route('/', methods=['POST'])
    def criar_reserva():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        num_sala = dados.get("num_sala")
        lab = True if dados.get("lab") == "True" else False
        data = dados.get("data")
        turma_id = dados.get("turma_id")

        if (num_sala == None or lab == None or data == None or turma_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        
        data = datetime.strptime(data, "%d/%m/%Y").date()

        registro_reservas = Reserva.query.filter_by(data=data)
        if registro_reservas:
            for reserva in registro_reservas:
                if (num_sala == reserva.num_sala):
                    mensagem = {"Erro": "Sala Já Reservada nessa Data!"}
                    return jsonify(mensagem), 409
        
        # Requisição para SchoolManaganer API para acessar Turmas
        response = requests.get("http://schoolmanager:5000/turmas/{}".format(turma_id))

        if response.status_code != 200:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 422

        nova_reserva = Reserva(
            num_sala = num_sala,
            lab = lab, 
            data = data,
            turma_id = turma_id
        )

        db.session.add(nova_reserva)
        db.session.commit()

        mensagem = {"Mensagem": "Reserva Efetuada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    @reservas_bp.route('/<int:reserva_id>', methods=['PUT'])
    def atualizar_reserva(reserva_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400
        
        reserva = Reserva.query.get(reserva_id)
        if reserva is None:
            mensagem = {"Erro": "Reserva Não Cadastrada!"}
            return jsonify(mensagem), 404

        num_sala = dados.get("num_sala")
        lab = True if dados.get("lab") == "True" else False
        data = dados.get("data")
        turma_id = dados.get("turma_id")

        if (num_sala == None or lab == None or data == None or turma_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400
        
        data = datetime.strptime(data, "%d/%m/%Y").date()

        registro_reservas = Reserva.query.filter_by(data=data)
        if registro_reservas:
            for reserva in registro_reservas:
                if (num_sala == reserva.num_sala and reserva_id != reserva.id):
                    mensagem = {"Erro": "Sala Já Reservada nessa Data!"}
                    return jsonify(mensagem), 409
        
        # Requisição para SchoolManaganer API para acessar Turmas
        response = request.get("http://schoolmanager:5000/turmas/{}".format(turma_id))

        if response.status_code != 200:
            mensagem = {"Erro": "Turma Não Cadastrada!"}
            return jsonify(mensagem), 422

        reserva.num_sala = num_sala
        reserva.lab = lab
        reserva.data = data
        reserva.turma_id = turma_id

        db.session.commit()

        mensagem = {"Mensagem": "Reserva Atualizada com Sucesso!"}
        return jsonify(mensagem), 200
        
    @staticmethod
    @reservas_bp.route('/<int:reserva_id>', methods=['DELETE'])
    def deletar_reserva(reserva_id):
        """
        Delete os dados de uma reserva específica com base no ID informado

        Parâmetros:
            reserva_id (int): ID da reserva a ser deletada

        Retorna:
            - Se a reserva for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma reserva pelo ID usando SQLAlchemy e salva em reserva
        reserva = Reserva.query.get(reserva_id)

        # Se a reserva não for encontrada
        if reserva is None:
            mensagem = {"Erro": "Reserva Não Cadastrada!"}
            return jsonify(mensagem), 404
            
        # Deletar registro no Banco de Dados
        db.session.delete(reserva)
        db.session.commit()
            
        mensagem = {"Mensagem": "Reserva Cancelada com Sucesso!"}
        return jsonify(mensagem), 200