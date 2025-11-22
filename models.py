from pydantic import BaseModel

# Modelos de Dados
class UserQuery(BaseModel):
    pergunta: str

class BotResponse(BaseModel):
    resposta: str