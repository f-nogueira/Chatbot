from fastapi import APIRouter, HTTPException
from models import UserQuery, BotResponse
from services import query_llm

router = APIRouter()

@router.post("/chat", response_model=BotResponse)
async def chat_endpoint(query: UserQuery):
    """
    Rota principal do Chatbot.
    Recebe a pergunta, processa via RAG (Service) e devolve a resposta.
    """
    resposta_ia = query_llm(query.pergunta)
    return BotResponse(resposta=resposta_ia)

@router.get("/health")
async def health_check():
    """
    Rota para verificar se a API está no ar.
    """
    return {"status": "ok"}