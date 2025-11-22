# Arquivo: ./frontend/Dockerfile

FROM node:18-alpine

WORKDIR /app

# Copia os arquivos de configuração do Node
COPY package.json package-lock.json* ./

# Instala as dependências
RUN npm install

# Copia o código do React
COPY . .

# Expõe a porta do Vite
EXPOSE 5173

# O --host é OBRIGATÓRIO para o Docker expor o site para fora do container
CMD ["npm", "run", "dev", "--", "--host"]