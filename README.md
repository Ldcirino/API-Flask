

## Como rodar localmente :D

1. Criar venv e instalar:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Inicializar banco e migrar:
   export FLASK_APP=manage.py
   flask db init
   flask db migrate -m "initial"
   flask db upgrade

3. Rodar:
   flask run --host=0.0.0.0 --port=5000
   # ou via docker-compose up --build

Endpoints básicos:
GET  /api/professores
POST /api/professores
GET  /api/professores/<id>
PUT  /api/professores/<id>
DELETE /api/professores/<id>

Mesmos padrões para /api/turmas e /api/alunos

Swagger UI: /apidocs (rodando localmente)