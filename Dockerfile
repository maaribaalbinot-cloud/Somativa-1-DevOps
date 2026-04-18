#Definindo a imagem base do Python
FROM python:3.10-slim

#Definindo o diretório de trabalho dentro do container
WORKDIR /app

#Copiando o arquivo de requisitos para o container e instalando as dependências
COPY requirements.txt .

#Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

#Copiando o restante dos arquivos do projeto para o container
COPY . .

#Expondo a porta que a aplicação irá rodar
EXPOSE 5000

#Definindo o comando para rodar a aplicação
CMD ["python", "app.py"]