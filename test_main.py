from fastapi.testclient import TestClient
from main import app
import sqlite3
import os
from services import get_estoque_as_text 

client = TestClient(app)

# Teste 1: Verificar se a API está no ar
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Teste 2: Verificar se a recuperação do banco de dados está retornando texto (Contexto do RAG)
def test_get_estoque_retorna_texto():
    # Garante que o banco existe criando a tabela na mão caso não exista
    conn = sqlite3.connect("floricultura.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cor TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.close()
    
    # Chama a função que agora mora no services.py
    texto = get_estoque_as_text()
    
    assert isinstance(texto, str) # Deve ser uma string
    assert "ESTOQUE ATUAL" in texto