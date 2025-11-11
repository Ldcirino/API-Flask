
<h2 id="arquitetura">🧩 Arquitetura do Sistema</h2>
📦SchoolMicroservices<br>
 ┣ 🧩SchoolActivitiesAPI<br>
 ┃ ┣ 📂controllers<br>
 ┃ ┃ ┣ 📜atividade_controller.py<br>
 ┃ ┃ ┗ 📜nota_controller.py<br>
 ┃ ┣ 📂models<br>
 ┃ ┃ ┣ 📜__init__.py<br>
 ┃ ┃ ┣ 📜atividade.py<br>
 ┃ ┃ ┗ 📜nota.py<br>
 ┃ ┣ 🚀app.py<br>
 ┃ ┣ ⚙️config.py<br>
 ┃ ┣ 🐳Dockerfile<br>
 ┃ ┣ 📖README.md<br>
 ┃ ┣ 📦requirements.txt<br>
 ┃ ┗ 📑swagger.yml<br>
 ┣ 🧩SchoolManagerAPI<br>
 ┃ ┣ 📂controllers<br>
 ┃ ┃ ┣ 📜aluno_controller.py<br>
 ┃ ┃ ┣ 📜professor_controller.py<br>
 ┃ ┃ ┗ 📜turma_controller.py<br>
 ┃ ┣ 📂models<br>
 ┃ ┃ ┣ 📜__init__.py<br>
 ┃ ┃ ┣ 📜aluno.py<br>
 ┃ ┃ ┣ 📜professor.py<br>
 ┃ ┃ ┗ 📜turma.py<br>
 ┃ ┣ 📜.gitignore<br>
 ┃ ┣ 🚀app.py<br>
 ┃ ┣ ⚙️config.py<br>
 ┃ ┣ 🐳Dockerfile<br>
 ┃ ┣ 📜LICENSE<br>
 ┃ ┣ 📖README.md<br>
 ┃ ┣ 📦requirements.txt<br>
 ┃ ┗ 📑swagger.yml<br>
 ┣ 🧩SchoolReservationAPI<br>
 ┃ ┣ 📂controllers<br>
 ┃ ┃ ┗ 📜reserva_controller.py<br>
 ┃ ┣ 📂models<br>
 ┃ ┃ ┣ 📜__init__.py<br>
 ┃ ┃ ┗ 📜reserva.py<br>
 ┃ ┣ 🚀app.py<br>
 ┃ ┣ ⚙️config.py<br>
 ┃ ┣ 🐳Dockerfile<br>
 ┃ ┣ 📖README.md<br>
 ┃ ┣ 📦requirements.txt<br>
 ┃ ┗ 📑swagger.yml<br>
 ┣ 🚫.gitignore<br>
 ┣ 🐳docker-compose.yml<br>
 ┣ ⚖️LICENSE<br>
 ┗ 📖README.md<br>
