from app.controllers.aluno import bp as alunos_bp
from app.controllers.professor import bp as professores_bp
from app.controllers.turma import bp as turmas_bp
from flask import jsonify
from app.crud_routes import register_crud_routes

def register_routes(app):
    app.register_blueprint(alunos_bp)
    app.register_blueprint(professores_bp)
    app.register_blueprint(turmas_bp)
    register_crud_routes(app)
    
    @app.route('/api/health')
    def health():
       return jsonify({'status': 'ok'})