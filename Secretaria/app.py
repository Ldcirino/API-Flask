from flask import Flask         # Para importar a classe principal Flask
from flasgger import Swagger    # Para gerar a documentação da API
from config import Config
from models import db
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.turma_controller import TurmaController


# Cria a instância principal da aplicação Flask
app = Flask(__name__)

# Carrega as configurações definidas na classe Config
app.config.from_object(Config)

# Inicializa o Swagger para gerar a documentação da API com base no arquivo swagger.yml
swagger = Swagger(app, template_file='swagger.yml')

# Inicializa o SQLAlchemy, conectando o ORM à aplicação Flask
db.init_app(app)

# Cria Tabelas do Banco de Dados
with app.app_context():
    db.create_all()

# Rotas Alunos
# Lista todos os alunos (método GET)
app.add_url_rule("/alunos", view_func=AlunoController.listar_alunos, methods=["GET"])

# Exibe um aluno específico pelo ID (método GET)
app.add_url_rule("/alunos/<int:aluno_id>", view_func=AlunoController.exibir_aluno, methods=["GET"])

# Cria um novo aluno (método POST)
app.add_url_rule("/alunos", view_func=AlunoController.criar_aluno, methods=["POST"])

# Atualiza os dados de um aluno existente pelo ID (método PUT)
app.add_url_rule("/alunos/<int:aluno_id>", view_func=AlunoController.atualizar_aluno, methods=["PUT"])

# Deleta um aluno pelo ID (método DELETE)
app.add_url_rule("/alunos/<int:aluno_id>", view_func=AlunoController.deletar_aluno, methods=["DELETE"])

# Rotas Professores
# Lista todos os professores (método GET)
app.add_url_rule("/professores", view_func=ProfessorController.listar_professores, methods=["GET"])

# Exibe um professor específico pelo ID (método GET)
app.add_url_rule("/professores/<int:professor_id>", view_func=ProfessorController.exibir_professor, methods=["GET"])

# Cria um novo professor (método POST)
app.add_url_rule("/professores", view_func=ProfessorController.criar_professor, methods=["POST"])

# Atualiza os dados de um professor existente pelo ID (método PUT)
app.add_url_rule("/professores/<int:professor_id>", view_func=ProfessorController.atualizar_professor, methods=["PUT"])

# Deleta um professor pelo ID (método DELETE)
app.add_url_rule("/professores/<int:professor_id>", view_func=ProfessorController.deletar_professor, methods=["DELETE"])

# Rotas Turmas
# Lista todas as turmas (método GET)
app.add_url_rule("/turmas", view_func=TurmaController.listar_turmas, methods=["GET"])

# Exibe uma turma específica pelo ID (método GET)
app.add_url_rule("/turmas/<int:turma_id>", view_func=TurmaController.exibir_turma, methods=["GET"])

# Cria uma nova turma (método POST)
app.add_url_rule("/turmas", view_func=TurmaController.criar_turma, methods=["POST"])

# Atualiza os dados de uma turma existente pelo ID (método PUT)
app.add_url_rule("/turmas/<int:turma_id>", view_func=TurmaController.atualizar_turma, methods=["PUT"])

# Deleta uma turma pelo ID (método DELETE)
app.add_url_rule("/turmas/<int:turma_id>", view_func=TurmaController.deletar_turma, methods=["DELETE"])

# Executar código quando o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=False, port=5000)  # Definindo porta 5000 para rodar API