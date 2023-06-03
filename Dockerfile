# Use a imagem oficial do Python como base
FROM python:3

# Defina a variável de ambiente PYTHONUNBUFFERED para garantir que os logs do Python sejam enviados para o console
#ENV PYTHONUNBUFFERED=1

# Crie um diretório de trabalho e defina-o como o diretório de trabalho padrão
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt /app/

# Instale as dependências do projeto
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir snscrape fastapi uvicorn
RUN pip3 install --upgrade git+https://github.com/JustAnotherArchivist/snscrape.git

# Copie o restante do código do projeto para o diretório de trabalho
COPY . /app/