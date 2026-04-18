from flask import Flask, render_template_string
import random
import json

app = Flask(__name__)

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

@app.route('/pergunta')
def pergunta():
    p = random.choice(dados)

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

    return render_template_string(html)

if __name__ == '__main__':
    print("Aplicação pronta para execução")
    # Esta linha abaixo é a que mantém o servidor ligado!
    app.run(debug=True, host='0.0.0.0', port=5000)