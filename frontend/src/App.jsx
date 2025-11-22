import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [input, setInput] = useState('')
  const [mensagens, setMensagens] = useState([
    { texto: "Olá! Sou o assistente da Floricultura. Pergunte sobre nosso estoque!", remetente: 'bot' }
  ])
  const [carregando, setCarregando] = useState(false)

  const enviarMensagem = async () => {
    if (!input.trim()) return

    // 1. Adiciona a mensagem do usuário na tela
    const novaMensagemUsuario = { texto: input, remetente: 'user' }
    setMensagens(prev => [...prev, novaMensagemUsuario])
    setCarregando(true)
    const mensagemAtual = input
    setInput('') // Limpa o campo

    try {
      // 2. Manda para o Backend (FastAPI)
      const response = await axios.post('http://127.0.0.1:8000/chat', {
        pergunta: mensagemAtual
      })

      // 3. Adiciona a resposta da IA na tela
      const novaMensagemBot = { texto: response.data.resposta, remetente: 'bot' }
      setMensagens(prev => [...prev, novaMensagemBot])
      
    } catch (error) {
      console.error("Erro:", error)
      const msgErro = { texto: "Erro ao conectar com o servidor. O Backend está rodando?", remetente: 'bot' }
      setMensagens(prev => [...prev, msgErro])
    } finally {
      setCarregando(false)
    }
  }

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>🌸 Floricultura AI</h1>
      </div>
      
      <div className="chat-box">
        {mensagens.map((msg, index) => (
          <div key={index} className={`mensagem ${msg.remetente}`}>
            <p>{msg.texto}</p>
          </div>
        ))}
        {carregando && <div className="mensagem bot"><p>Digitando...</p></div>}
      </div>

      <div className="input-area">
        <input 
          type="text" 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && enviarMensagem()}
          placeholder="Pergunte sobre rosas, tulipas..."
        />
        <button onClick={enviarMensagem} disabled={carregando}>
          Enviar
        </button>
      </div>
    </div>
  )
}

export default App