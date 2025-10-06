
from app import create_app
from database import db
from app.models import aluno, professor, turma

app = create_app() 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
