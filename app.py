from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

@app.route('/pergunta')
def pergunta_aleatoria():
    return jsonify(random.choice(dados))

@app.route('/todas')
def todas_perguntas():
    return jsonify(dados)

@app.route('/resposta/<int:id>')
def resposta(id):
    for item in dados:
        if item["id"] == id:
            return jsonify({"resposta": item["resposta"]})
    return jsonify({"erro": "Pergunta não encontrada"})

app.run(debug=True)