# Somativa-1
# API DevOps

Projeto criado para a atividade somativa da disciplina DevOps do curso de Análise e Desenvolvimento de Sistemas da PUCPR. 
Consiste no desenvolvimento de uma API simples para auxiliar no estudo da disciplina, permitindo o acesso a perguntas e respostas sobre conceitos importantes da área. Além disso, o projeto foi criado para praticar o uso de controle de versão com Git, incluindo a criação de branches, commits e pull requests.

## Funcionalidades
- Retornar uma pergunta aleatória sobre DevOps
- Listar todas as perguntas disponíveis
- Buscar a resposta de uma pergunta específica pelo ID

## Rotas
- /pergunta → retorna uma pergunta aleatória
- /todas → retorna todas as perguntas
- /resposta/{id} → retorna a resposta da pergunta informada

## Tecnologias Utilizadas
Python
Flask
Git

## Como rodar
pip install flask
python app.py
http://localhost:5000/pergunta

## Considerações
Este é um projeto acadêmico simples, desenvolvido com foco no aprendizado de práticas de DevOps e versionamento de código.