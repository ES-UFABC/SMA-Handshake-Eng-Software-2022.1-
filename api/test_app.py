import json
import random
import string

from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_consumidores():
    response = client.get("usuarios/consumidores")
    assert response.status_code == 200


def test_get_produtores():
    response = client.get("usuarios/produtores")
    assert response.status_code == 200


def test_get_produtos_commodities():
    response = client.get("produtos/commodities")
    assert response.status_code == 200


def test_get_produtos_ofertas():
    response = client.get("produtos/ofertas")
    assert response.status_code == 200


def test_get_produtos_ordem():
    response = client.get("produtos/ordem")
    assert response.status_code == 200


def test_post_usuarios_cadastrar():
    letters = string.ascii_lowercase
    email_fake = ''.join(random.choice(letters) for i in range(10)) + \
        '@teste.com'

    registro_usuario = """{ 
                "tipo": "produtor",
                "nome": "novo",
                "cpf_cnpj": "99988877766",
                "telefone": "1122224444",
                "estado": "SP",
                "cidade": "Teste",
                "complemento": "teste",
                "cep": "12345678",
                "logradouro": "teste",
                "numero": "20",
                "email": "%s",
                "senha": "1234"
    }""" % (email_fake)

    x = json.loads(registro_usuario)
    response = client.post("usuarios/cadastrar", json=x)

    assert response.status_code == 200


def test_post_usuarios_cadastrar_email_cadastrado():
    registro_usuario = """{ 
                "tipo": "produtor",
                "nome": "novo",
                "cpf_cnpj": "99988877766",
                "telefone": "1122224444",
                "estado": "SP",
                "cidade": "Teste",
                "complemento": "teste",
                "cep": "12345678",
                "logradouro": "teste",
                "numero": "20",
                "email": "consumidor1@teste.com.br",
                "senha": "1234"
    }"""

    x = json.loads(registro_usuario)
    response = client.post("usuarios/cadastrar", json=x)

    assert response.status_code == 404


def test_post_usuarios_login_correto():
    login = """{
        "email": "consumidor1@teste.com.br",
        "senha": "senha"
    }"""

    x = json.loads(login)
    response = client.post("usuarios/login", json=x)

    assert response.status_code == 200


def test_post_usuarios_login_incorreto():
    login = """{
        "email": "consumidor9090@teste.com.br",
        "senha": "senha"
    }"""

    x = json.loads(login)
    response = client.post("usuarios/login", json=x)

    assert response.status_code == 404


def test_post_produtos_cadastrar():
    produtos = """{
        "nome": "teste"
    }"""

    x = json.loads(produtos)
    response = client.post("produtos/cadastrar", json=x)

    assert response.status_code == 200
