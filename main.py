from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import router 

# Inicialização
app = FastAPI(title="Floricultura AI Chatbot")

# Banco de Dados
init_db()

# Configuração de CORS (Segurança/Acesso)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ligação do arquivo routes.py ao app principal
app.include_router(router)