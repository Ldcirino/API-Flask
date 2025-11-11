
<h2 id="requisitos">📦 Requisitos</h2>

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.13.2-blue" alt="Python = 3.13.2"><br>

Tenha o Docker instalado caso queria rodar o projeto num container

No diretório raiz do projeto, construa a imagem do container
```bash
docker build -t school-manager .
```
Execute o container
```bash
docker run --name school-manager-container -p 5000:5000 school-manager
```

Para rodar localmente sem ser via container tenho o Python instalado e no diretório raiz do projeto execute o comando para instalar as bibliotecas<br>

```bash
pip install -r requirements.txt
```

<h2 id="how-it-works">⚙️ Funcionalidades</h2>
🔹 CRUD de Alunos (Cadastro, Listagem, Atualização e Exclusão)
<br>🔹 CRUD de Professors (Cadastro, Listagem, Atualização e Exclusão)
<br>🔹 CRUD de Turmas (Cadastro, Listagem, Atualização e Exclusão)

<h2 id="endpoints">🛠️ Endpoints da API</h2>

Documentação Swagger
```bash
curl -X GET http://localhost:5000/apidocs
```
Listagem de Professores
```bash
curl -X GET http://localhost:5000/professores
```
Cadastro de Professor
```bash
curl -X POST http://localhost:5000/professores \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Carlos",
          "idade":"32", 
          "materia":"Microserviços",
          "observacoes":""
        }'
```
Exibir Professor
```bash
curl -X GET http://localhost:5000/professores/{professor_id}
```
Atualizar Professor
```bash
curl -X PUT http://localhost:5000/professores/{professor_id} \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Carlos",
          "idade":"32", 
          "materia":"Mobile",
          "observacoes":""
        }'
```
Deletar Professor
```bash
curl -X DELETE http://localhost:5000/professores/{professor_id}
```
Listagem de Turmas
```bash
curl -X GET http://localhost:5000/turmas
```
Cadastro de Turma
```bash
curl -X POST http://localhost:5000/turmas \
    -H "Content-Type: application/json" \
    -d '{
          "descricao":"ADS Periodo Manha", 
          "ativo":"True",
          "professor_id":"1"
        }'
```
Exibir Turma
```bash
curl -X GET http://localhost:5000/turmas/{turma_id}
```
Atualizar Turma
```bash
curl -X PUT http://localhost:5000/turmas/{turma_id} \
    -H "Content-Type: application/json" \
    -d '{
          "descricao":"ADS Periodo Manha", 
          "ativo":"False",
          "professor_id":"1"
        }'
```
Deletar Turma
```bash
curl -X DELETE http://localhost:5000/turmas/{turma_id}
```
Listagem de Alunos
```bash
curl -X GET http://localhost:5000/alunos
```
Cadastro de Alunos
```bash
curl -X POST http://localhost:5000/alunos \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Lucas",
          "idade":"27", 
          "data_nasc":"18/11/1998",
          "turma_id":"1"
        }'
```
Exibir Aluno
```bash
curl -X GET http://localhost:5000/alunos/{aluno_id}
```
Atualizar Aluno
```bash
curl -X PUT http://localhost:5000/alunos/{aluno_id} \
    -H "Content-Type: application/json" \
    -d '{
          "nome":"Lucas",
          "idade":"27", 
          "data_nasc":"18/11/1998",
          "turma_id":"1"
        }'
```
Deletar Alunos
```bash
curl -X DELETE http://localhost:5000/alunos/{aluno_id}
```

<h2 id="licença">📜 Licença</h2>
Este projeto é para fins educacionais e está disponível sob a <a href="./LICENSE">Licença MIT.</a>
