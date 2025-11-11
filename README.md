
## 👨‍💻 Integrantes do Grupo

| Nome | RA |
|------|------|
| **Leonardo Diniz Cirino** | 2202296 |
| **Felipe Oliveira** | 2404017 |
| **Rafael Bela Ferracini** | 2403329 |
| **Gustavo Bezerra** | 2403495 |

---

# 🏫 Sistema de Gerenciamento Acadêmico

Um sistema completo para **gerenciar alunos, professores, cursos, turmas, disciplinas, matrículas, notas e atividades**.  
Desenvolvido em **Python** utilizando **Flask** e **SQLAlchemy**, o projeto oferece uma arquitetura organizada e extensível para instituições de ensino.

---

## 🚀 Funcionalidades Principais

✅ **Gerenciamento de Alunos**  
- Cadastro, edição, listagem e exclusão de alunos  
- Associação com turmas, cursos e notas  

✅ **Gerenciamento de Professores**  
- Cadastro e edição de professores  
- Associação com disciplinas e turmas  

✅ **Gerenciamento de Cursos e Disciplinas**  
- Criação e vinculação de disciplinas a cursos  
- Controle de carga horária  

✅ **Turmas e Matrículas**  
- Criação e gerenciamento de turmas  
- Matrícula de alunos em turmas e disciplinas  

✅ **Notas e Atividades**  
- Registro e atualização de notas  
- Controle de atividades avaliativas  

✅ **Banco de Dados Relacional**  
- Persistência de dados com **SQLAlchemy ORM**  
- Estrutura de tabelas bem definida (alunos, professores, cursos, disciplinas, turmas, matrículas, notas)

---

## 🧱 Estrutura do Projeto

```
📦 Projeto-Gerenciamento-Academico
├── database.py        # Configuração do banco de dados (SQLAlchemy)
├── models.py          # Definição das classes e relacionamentos
├── services.py        # Lógica de negócio (CRUDs e validações)
├── main.py            # Menu principal e interface de interação
└── README.md          # Documentação do projeto
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask**
- **SQLAlchemy**
- **SQLite**
- **Docker** *(opcional)*

---

## 🧩 Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)
- (opcional) [Docker](https://www.docker.com/)

---

## 🛠️ Instalação e Execução

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   cd NOME-DO-REPOSITORIO
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate        # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o projeto**
   ```bash
   python main.py
   ```

---

## 💾 Banco de Dados

O sistema utiliza **SQLAlchemy ORM** para mapear as entidades.  
Por padrão, o banco de dados é um arquivo `sqlite.db` gerado automaticamente.

Você pode alterar o tipo de banco (ex: MySQL, PostgreSQL) no arquivo `database.py`.

---

## 📚 Modelos Principais

| Entidade      | Atributos Principais |
|----------------|----------------------|
| **Aluno**      | nome, cpf, data_nascimento, curso_id |
| **Professor**  | nome, cpf, especialidade |
| **Curso**      | nome, carga_horaria |
| **Disciplina** | nome, carga_horaria, curso_id |
| **Turma**      | nome, disciplina_id, professor_id |
| **Matrícula**  | aluno_id, turma_id, data_matricula |
| **Nota**       | matricula_id, valor, tipo_atividade |

---

## 🧪 Exemplo de Uso

**Exemplo de cadastro de aluno via menu interativo:**

```
1 - Cadastrar Aluno
2 - Listar Alunos
3 - Editar Aluno
4 - Excluir Aluno
Escolha uma opção: 1
Nome do aluno: João Silva
CPF: 123.456.789-00
Data de nascimento: 2002-04-10
Aluno cadastrado com sucesso!
```

---

## 🧱 Próximos Passos (To-do List)

- [ ] Implementar interface web com Flask  
- [ ] Criar autenticação para administradores e professores  
- [ ] Adicionar relatórios em PDF e Excel  
- [ ] Criar API REST para integração externa  
- [ ] Adicionar testes automatizados  

---