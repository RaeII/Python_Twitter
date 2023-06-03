FROM ubuntu:latest

# Atualiza os pacotes e instala o Python e o pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y git

# Defina a variável de ambiente PYTHONUNBUFFERED para garantir que os logs do Python sejam enviados para o console
#ENV PYTHONUNBUFFERED=1

# Crie um diretório de trabalho e defina-o como o diretório de trabalho padrão
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt /app/

# Instale as dependências do projeto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . /app/