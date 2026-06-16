# 🤖 Dan - Mentor de Dados (AI Assistant)

Um assistente virtual inteligente desenvolvido com a API do Google Gemini e interface web em Streamlit. O Dan atua como um mentor educacional especializado em Métricas de BI, Otimização SQL e Python (Pandas vs Polars), utilizando técnicas avançadas de Engenharia de Prompt e injeção de contexto para fornecer respostas precisas.

## 🚀 Principais Funcionalidades

* **Interface de Chat Interativa:** Construída com Streamlit, simulando uma experiência fluida de mensageria.
* **Memória de Conversa (Session State):** Retenção de histórico de chat e gerenciamento de estado do servidor para evitar quedas de conexão com a API.
* **Engenharia de Prompt & Árvores de Decisão:** O modelo de IA segue um prompt sistêmico estruturado para decidir quando usar o conhecimento injetado (*Cenário A*), quando usar seu conhecimento geral para tecnologia (*Cenário B*) e quando bloquear assuntos fora do escopo (*Cenário C*).
* **Aterramento de IA (Grounding/RAG Básico):** O assistente consome documentos `.txt` locais para embasar suas respostas em diretrizes de negócios pré-aprovadas.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Streamlit** (Front-end e Web App)
* **Google GenAI SDK** (Modelo `gemini-2.5-flash`)
* **python-dotenv** (Gerenciamento seguro de credenciais)

## ⚙️ Como executar o projeto localmente

1. **Clone este repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd dan-assistant
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv .venv
# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
```

3. **Instale as bibliotecas necessárias:**
```bash
pip install streamlit google-genai python-dotenv
```

4. **Configure a Chave de API:**
Crie um arquivo `.env` na raiz do projeto e insira a sua chave do Google Gemini:
```env
GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

5. **Inicie a aplicação:**
```bash
streamlit run src/app.py
```