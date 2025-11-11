<h1 align="center"; style="font-weight: bold;">School Activities API</h1>

<h3 align="center"><img  alt="Faculdade Impacta" width = "400px" src="https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png"></h3>

<p>
    <img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status = Concluído">
    <img src="https://img.shields.io/badge/Documentação-Completa-brightgreen" alt="Documentação: Completa">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License = MIT">
</p>

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

<p align="center">
    <a href="#sobre">Sobre</a> • 
    <a href="#requisitos">Requisitos</a> •
    <a href="#how-it-works">Funcionalidades</a> •
    <a href="#endpoints">Endpoints da API</a> •
</p>

<h2 id="sobre">📖 Sobre</h2>
API referente ao Projeto Acadêmico da Disciplina de Desenvolvimento de APIs e Microsserviços, ministrada pelo professor Giovani Bontempo na Faculdade Impacta, durante o terceiro semestre do curso Análise e Desenvolvimento de Sistemas cursado no 2º Semestre de 2025.
<br><br>O projeto consiste em uma API RESTful construída com Flask para realizar o gerenciamento de Atividades e Notas de uma instituição de ensino.
<br>

<h2 id="requisitos">📦 Requisitos</h2>

[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) <img src="https://img.shields.io/badge/python-3.13.2-blue" alt="Python = 3.13.2"><br>

Tenha o Docker instalado caso queria rodar o projeto num container

No diretório raiz do projeto, construa a imagem do container
```bash
docker build -t school-activities .
```
Execute o container
```bash
docker run --name school-activities-container -p 5001:5001 school-activities
```

Para rodar localmente sem ser via container tenho o Python instalado e no diretório raiz do projeto execute o comando para instalar as bibliotecas<br>

```bash
pip install -r requirements.txt
```

<h2 id="how-it-works">⚙️ Funcionalidades</h2>
🔹 CRUD de Atividades (Cadastro, Listagem, Atualização e Exclusão)
<br>🔹 CRUD de Notas (Cadastro, Listagem, Atualização e Exclusão)

<h2 id="endpoints">🛠️ Endpoints da API</h2>

Documentação Swagger
```bash
curl -X GET http://localhost:5001/apidocs
```
Listagem de Atividades
```bash
curl -X GET http://localhost:5001/atividades
```
Cadastro de Atividade
```bash
curl -X POST http://localhost:5001/atividades \
    -H "Content-Type: application/json" \
    -d '{
            "nome_atividade": "Laboratório",
            "descricao": "Laboratorio de Redes",
            "peso_porcentagem": "1",
            "data_entrega": "05/11/2025",
            "turma_id": "1",
            "professor_id": 1
        }'
```
Exibir Atividade
```bash
curl -X GET http://localhost:5001/atividades/{atividade_id}
```
Atualizar Atividade
```bash
curl -X PUT http://localhost:5001/atividades/{atividade_id} \
    -H "Content-Type: application/json" \
    -d '{
            "nome_atividade": "Labpratório de Redes 1",
            "descricao": "Laboratorio de Redes",
            "peso_porcentagem": "1",
            "data_entrega": "06/11/2025",
            "turma_id": "1",
            "professor_id": 1
        }'
```
Deletar Atividade
```bash
curl -X DELETE http://localhost:5001/atividades/{atividade_id}
```
Listagem de Notas
```bash
curl -X GET http://localhost:5001/notas
```
Cadastro de Nota
```bash
curl -X POST http://localhost:5001/notas \
    -H "Content-Type: application/json" \
    -d '{
            "nota": "10",
            "aluno_id": "1",
            "atividade_id": "1"    
        }'
```
Exibir Nota
```bash
curl -X GET http://localhost:5001/notas/{nota_id}
```
Atualizar Nota
```bash
curl -X PUT http://localhost:5001/notas/{nota_id} \
    -H "Content-Type: application/json" \
    -d '{
            "nota": "8",
            "aluno_id": "1",
            "atividade_id": "1" 
        }'
```
Deletar Nota
```bash
curl -X DELETE http://localhost:5001/notas/{nota_id}
```
