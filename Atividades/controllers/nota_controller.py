from flask import Blueprint, jsonify, request
import requests
from models import db
from models.nota import Nota
from models.atividade import Atividade


# Classe responsável por controlar as ações relacionadas as notas
class NotaController:
    
    # Usando Blueprint para organinar Rotas
    notas_bp = Blueprint('notas', __name__)

    @staticmethod
    @notas_bp.route('/', methods=['GET'])
    def listar_notas():
        """
        Lista todas as notas cadastradas no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de notas e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Notas" usando SQLAlchemy e salva em notas
        notas = Nota.query.all()

        # Se houver notas cadastradas
        if notas:
            lista = []
            for nota in notas:
                # Converte para dicionario e adiciona na lista
                lista.append(nota.para_dicionario())
            return jsonify(lista), 200
        # Se não houver notas cadastradas
        else:
            mensagem = {"Erro": "Lista de Notas Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @notas_bp.route('/<int:nota_id>', methods=['GET'])
    def exibir_nota(nota_id):
        """
        Exibe os dados de uma nota específica com base no ID informado

        Parâmetros:
            nota_id (int): ID da nota a ser consultada

        Retorna:
            - Se a nota for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma nota pelo ID usando SQLAlchemy e salva em nota 
        nota = Nota.query.get(nota_id)

        # Se a nota for encontrada
        if nota:
            # Converte para dicionario e retorna como JSON
            return jsonify(nota.para_dicionario()), 200
        # Se a nota não existir no banco de dados
        else:
            mensagem = {"Erro": "Nota Não Cadastrada!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @notas_bp.route('/', methods=['POST'])
    def criar_nota():
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400

        nota = dados.get("nota")
        aluno_id = dados.get("aluno_id")
        atividade_id = dados.get("atividade_id")

        if (nota == None or aluno_id == None or atividade_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400

        registro_atividade = Atividade.query.filter_by(id=atividade_id)
        if not registro_atividade:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 422
        
        # Requisição para SchoolManaganer API para acessar Aluno
        response = requests.get("http://schoolmanager:5000/alunos/{}".format(aluno_id))

        if response.status_code != 200:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 404

        nova_nota = Nota(
            nota = nota,
            aluno_id = aluno_id, 
            atividade_id = atividade_id
        )

        db.session.add(nova_nota)
        db.session.commit()

        mensagem = {"Mensagem": "Nota Cadastrada com Sucesso!"}
        return jsonify(mensagem), 201
    
    @staticmethod
    @notas_bp.route('/<int:nota_id>', methods=['PUT'])
    def atualizar_nota(nota_id):
        dados = request.json
        if not dados:
            return {"Erro": "Requisição Incorreta"}, 400
        
        nota = Atividade.query.get(nota_id)
        if nota is None:
            mensagem = {"Erro": "Nota Não Cadastrada!"}
            return jsonify(mensagem), 404

        nota_atualizada = dados.get("nota")
        aluno_id = dados.get("aluno_id")
        atividade_id = dados.get("atividade_id")

        if (nota_atualizada == None or aluno_id == None or atividade_id == None):
            mensagem = {"Erro": "Formulário Incompleto!"}
            return jsonify(mensagem), 400

        registro_atividade = Atividade.query.filter_by(id=atividade_id)
        if not registro_atividade:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 422
        
        # Requisição para SchoolManaganer API para acessar Aluno
        response = requests.get("http://schoolmanager:5000/alunos/{}".format(aluno_id))

        if response.status_code != 200:
            mensagem = {"Erro": "Aluno Não Cadastrado!"}
            return jsonify(mensagem), 424

        nota.nota = nota_atualizada
        nota.aluno_id = aluno_id
        nota.atividade_id = atividade_id

        db.session.commit()

        mensagem = {"Mensagem": "Nota Atualizada com Sucesso!"}
        return jsonify(mensagem), 200
        
    @staticmethod
    @notas_bp.route('/<int:nota_id>', methods=['DELETE'])
    def deletar_nota(nota_id):
        """
        Delete os dados de uma nota específica com base no ID informado

        Parâmetros:
            nota_id (int): ID da nota a ser deletada

        Retorna:
            - Se a nota for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma nota pelo ID usando SQLAlchemy e salva em nota
        nota = Nota.query.get(nota_id)

        # Se a nota não for encontrada
        if nota is None:
            mensagem = {"Erro": "Nota Não Cadastrada!"}
            return jsonify(mensagem), 404
            
        # Deletar registro no Banco de Dados
        db.session.delete(nota)
        db.session.commit()
            
        mensagem = {"Mensagem": "Nota Deletada com Sucesso!"}
        return jsonify(mensagem), 200