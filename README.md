# 🌸 Floricultura AI Chatbot (RAG + FastAPI + React)

Este projeto é um assistente virtual inteligente desenvolvido como Case Técnico. O objetivo é simular um atendimento de floricultura onde a Inteligência Artificial responde dúvidas sobre o estoque utilizando dados reais do banco de dados (SQLite), evitando alucinações através da técnica **RAG (Retrieval-Augmented Generation)**.

## 🚀 Tecnologias Utilizadas

O projeto foi construído com uma arquitetura moderna e modular:

- **Frontend:** React + Vite + Axios (Interface SPA responsiva)
- **Backend:** FastAPI (API REST de alta performance)
- **Banco de Dados:** SQLite (Persistência de dados relacional)
- **IA / LLM:** Hugging Face Inference API (Modelos Open Source como Qwen/Mistral)
- **Arquitetura:** MVC Simplificado (Separação de Rotas, Serviços e Modelos)

## 📂 Estrutura do Projeto

```text
chatbot/
├── .env                 # Variáveis de ambiente (Token de Segurança)
├── database.py          # Gerenciamento de conexão com SQLite
├── models.py            # Schemas Pydantic (Validação de dados)
├── routes.py            # Definição dos Endpoints da API
├── services.py          # Lógica de Negócio (RAG + Integração com IA)
├── main.py              # Configuração inicial da aplicação
├── requirements.txt     # Lista de dependências Python
└── frontend/            # Aplicação React (Interface)
```

## ⚙️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto no seu ambiente local.

### 1. Configuração do Backend (API)

Navegue até a pasta raiz do projeto:

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instala as dependências
pip install -r requirements.txt
```

🔐 **Configuração de Segurança (.env):**  
Crie um arquivo chamado `.env` na raiz do projeto e adicione seu token da Hugging Face:

```ini
HF_TOKEN=seu_token_aqui_sem_aspas
```

### 2. Configuração do Frontend (Interface)

Abra um novo terminal e entre na pasta do frontend:

```bash
cd frontend

# Instala as dependências do Node.js
npm install
```

## ▶️ Como Rodar a Aplicação

Para o sistema funcionar, é necessário manter dois terminais abertos simultaneamente.

**Terminal 1: Servidor Backend**

```bash
# Na raiz do projeto (com a venv ativada)
uvicorn main:app --reload
```
O servidor iniciará em: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Documentação automática (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Terminal 2: Cliente Frontend**

```bash
# Na pasta /frontend
npm run dev
```
O site estará acessível no link mostrado (geralmente [http://localhost:5173](http://localhost:5173))

## 🧪 Testes Automatizados

O projeto inclui testes para validar a conexão com o banco e a formatação dos dados para a IA.

```bash
# Na raiz do projeto
pytest
```

## 🧠 Fluxo da Arquitetura (RAG)

1. **Interação:** O usuário envia uma pergunta via React (ex: "Tem rosas?").
2. **Recuperação (Retrieval):** O Backend (`services.py`) consulta o banco SQL e transforma o estoque tabular em texto natural.
3. **Contextualização:** O sistema cria um prompt contendo o estoque real + a pergunta do usuário.
4. **Geração (Generation):** A LLM processa o prompt e gera uma resposta humanizada, baseada estritamente nos dados fornecidos.
5. **Resposta:** O Frontend exibe a mensagem final ao usuário.

---

Desenvolvido por Felipe Lima para Processo Seletivo de Desenvolvedor Python + IA.
