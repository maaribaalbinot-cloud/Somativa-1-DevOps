import unittest
from app import app
import json

class TestQuizAPI(unittest.TestCase):
    def setUp(self):
        # Configura o Flask para modo de teste
        self.app = app.test_client()
        self.app.testing = True

    # Teste 1: Verifica se a rota /pergunta está carregando (Status 200)
    def test_get_pergunta_status(self):
        response = self.app.get('/pergunta')
        self.assertEqual(response.status_code, 200)

    # Teste 2: Verifica se o conteúdo retornado contém a tag HTML do título
    def test_get_pergunta_content(self):
        response = self.app.get('/pergunta')
        self.assertIn(b'<title>Quiz DevOps</title>', response.data)

    # Teste 3: Verifica se o arquivo de dados existe e pode ser carregado
    def test_json_load(self):
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        self.assertIsInstance(dados, list)
        self.assertGreater(len(dados), 0)

    # Teste 4: Verifica se uma rota que não existe retorna 404
    def test_404_page(self):
        response = self.app.get('/rota-inexistente')
        self.assertEqual(response.status_code, 404)

    # Teste 5: Verifica se a pergunta sorteada tem os campos obrigatórios
    def test_pergunta_structure(self):
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        pergunta = dados[0]
        self.assertIn('pergunta', pergunta)
        self.assertIn('resposta', pergunta)