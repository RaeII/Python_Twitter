# Use a imagem oficial do Python como base
FROM python:3

# Defina a variável de ambiente PYTHONUNBUFFERED para garantir que os logs do Python sejam enviados para o console
#ENV PYTHONUNBUFFERED=1

# Crie um diretório de trabalho e defina-o como o diretório de trabalho padrão
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt /app/

# Instale as dependências do projeto
RUN apt update
RUN apt install python3
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . /app/