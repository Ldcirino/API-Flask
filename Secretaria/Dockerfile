# Definindo imagem do container como python na versão 3.13.2
FROM python:3.13.2

# Definindo diretório de trabalho do container
WORKDIR /app

# Copia o arquivo requirements.txt do diretório local para dentro do container
COPY requirements.txt .

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install -r requirements.txt

# Define a variável de ambiente que informa ao Flask qual arquivo deve ser executado como ponto de entrada da aplicação
# Sendo o arquivo app.py no diretório do projeto
ENV FLASK_APP=app.py

# Define o host em que o Flask vai rodar
# 0.0.0.0 permite acesso fora do container
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Copia todo o conteúdo do diretório atual do projeto para dentro do container
COPY . .

# Expõe a porta 5000, utilizada pelo servidor Flask
EXPOSE 5000

# Comando a ser executado quando o container iniciar, iniciando o Flask e executando app.py
CMD ["flask", "run"]