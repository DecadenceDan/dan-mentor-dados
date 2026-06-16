import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Carrega as chaves secretas do arquivo .env
load_dotenv()

# 1. Configuração da Interface Web
st.set_page_config(page_title="Dan - Mentor de Dados", page_icon="🤖")
st.title("🤖 Dan - Seu Mentor de Dados")

# 2. Carregamento Eficiente (Cache evita ler o arquivo no HD a cada clique)
@st.cache_data
def carregar_contexto():
    try:
        with open('data/base_conhecimento.txt', 'r', encoding='utf-8') as f:
            base = f.read()
        with open('docs/prompt_sistema.txt', 'r', encoding='utf-8') as f:
            prompt = f.read()
        return f"{prompt}\n\n=== BASE DE CONHECIMENTO AUTORIZADA ===\n{base}"
    except FileNotFoundError:
        st.error("❌ Erro: Arquivos base_conhecimento.txt ou prompt_sistema.txt não encontrados.")
        st.stop()

# 3. Inicialização da IA e da Memória (Session State)
def inicializar_chat():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error("❌ Variável GEMINI_API_KEY não encontrada no ambiente.")
        st.stop()

    # 1. Salva o "telefone" (client) na memória para a conexão não fechar
    if "client" not in st.session_state:
        st.session_state.client = genai.Client(api_key=api_key)

    # 2. Cria o chat usando o client que está salvo com segurança na memória
    if "chat_session" not in st.session_state:
        config = types.GenerateContentConfig(
            system_instruction=carregar_contexto(),
            temperature=0.3
        )
        st.session_state.chat_session = st.session_state.client.chats.create(
            model="gemini-2.5-flash",
            config=config
        )
    
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {"role": "assistant", "content": "Olá! Sou o Dan. Como posso te ajudar com os estudos hoje?"}
    ]
        
inicializar_chat()

# 4. Renderizar o Histórico de Mensagens na Tela
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Capturar e Processar a Nova Mensagem
prompt_usuario = st.chat_input("Digite sua dúvida sobre SQL, Python ou BI...")

if prompt_usuario:
    # Mostra a mensagem do usuário na hora
    st.session_state.mensagens.append({"role": "user", "content": prompt_usuario})
    with st.chat_message("user"):
        st.markdown(prompt_usuario)

    # Processa a resposta do Dan
    with st.chat_message("assistant"):
        with st.spinner("Analisando..."):
            try:
                # Envia para a API mantendo a mesma sessão salva no estado
                resposta = st.session_state.chat_session.send_message(prompt_usuario)
                st.markdown(resposta.text)
                
                # Salva a resposta da IA no histórico de tela
                st.session_state.mensagens.append({"role": "assistant", "content": resposta.text})
            except Exception as e:
                st.error(f"Ocorreu um erro na conexão: {e}")