#Importando bibliotecas
from flask import Flask, render_template_string
import random
import json

#Iniciando framework Flask
app = Flask(__name__)

#Leitura do JSON com as perguntas e respostas do quiz
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

#Rota para acessar o quiz no navegador
@app.route('/pergunta')
def pergunta():
    #Seleção aleatória de uma pergunta do quiz
    p = random.choice(dados)

    #Template HTML simples
    html = f"""
    <html>
        <head>
            <title>Quiz DevOps</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Questão {p['id']}</h2>
            <p><strong>{p['pergunta']}</strong></p>

            <button onclick="mostrarResposta()">Mostrar resposta</button>

            <p id="resposta" style="display:none; margin-top:20px;">
                {p['resposta']}
            </p>

            <p style="margin-top:30px; color: gray;">
                Atualize a página para uma nova pergunta
            </p>

            <script>
                function mostrarResposta() {{
                    document.getElementById("resposta").style.display = "block";
                }}
            </script>
        </body>
    </html>
    """

    #Retorna o HTLM no navegador
    return render_template_string(html)

if __name__ == '__main__':
    print("Aplicação pronta para execução")
    # Esta linha abaixo é a que mantém o servidor docker ligado
    app.run(debug=True, host='0.0.0.0', port=5000)