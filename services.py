import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from database import get_connection

# Carrega as variáveis do arquivo .env
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = "Qwen/Qwen2.5-7B-Instruct"

def get_estoque_as_text():
    """
    Função interna: Vai ao banco e formata o texto.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, cor, quantidade, preco FROM flores")
    flores = cursor.fetchall()
    conn.close()

    texto = "ESTOQUE ATUAL DA FLORICULTURA:\n"
    for flor in flores:
        texto += f"- {flor[0]} ({flor[1]}): {flor[2]} un, R$ {flor[3]:.2f}\n"
    return texto

def query_llm(pergunta: str):
    """
    Recebe APENAS a pergunta.
    O contexto é buscado aqui dentro automaticamente.
    """
    
    # O próprio service busca os dados (RAG)
    contexto = get_estoque_as_text()

    if not HF_TOKEN:
        return "Erro: Token HF não configurado no arquivo .env"

    client = InferenceClient(model=REPO_ID, token=HF_TOKEN)

    messages = [
        {
            "role": "system", 
            "content": f"Você é um assistente útil. Responda APENAS com base neste estoque: {contexto}. Seja educado e breve."
        },
        {
            "role": "user", 
            "content": pergunta
        }
    ]

    try:
        response = client.chat_completion(messages, max_tokens=200)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erro IA: {e}")
        return f"A IA está indisponível, mas aqui está o estoque:\n{contexto}"