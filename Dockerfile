# Imagem base
FROM python:3.12-slim

# Define diretório da aplicação
WORKDIR /app

# Copia todos os arquivos da aplicação
COPY . /app

# Atualiza pip e instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta que o Flask vai usar
EXPOSE 5000

# Variáveis de ambiente do Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Comando padrão para rodar o Flask
CMD ["python", "run.py"]
