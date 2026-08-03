import os
import streamlit as st
from google import genai
from google.genai import types

# 1. Configuração da página
st.set_page_config(
    page_title="Chatbot com Memória",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Chatbot com Inteligência Artificial")
st.write("Converse em tempo real com o Gemini. O histórico da conversa é mantido automaticamente!")

# 2. Inicialização do Cliente da API do Gemini
@st.cache_resource
def iniciar_cliente():
    minha_chave = os.environ.get("GEMINI_API_KEY")
    return genai.Client(api_key=minha_chave)

client = iniciar_cliente()

# 3. Inicialização da Memória da Sessão no Streamlit (st.session_state)
if "historico_mensagens" not in st.session_state:
    st.session_state.historico_mensagens = []

if "chat_session" not in st.session_state:
    # Cria a sessão de chat nativa da API com instrução do sistema
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Você é um assistente virtual prestativo, claro e objetivo. Responda em tom amigável.",
            temperature=0.3
        )
    )

# 4. Renderizar mensagens anteriores salvas no histórico
for mensagem in st.session_state.historico_mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# 5. Capturar nova mensagem digitada pelo usuário
prompt_usuario = st.chat_input("Digite sua mensagem...")

if prompt_usuario:
    # Exibe a mensagem do usuário imediatamente na tela
    with st.chat_message("user"):
        st.write(prompt_usuario)
    
    # Salva a mensagem do usuário no histórico local da tela
    st.session_state.historico_mensagens.append({"role": "user", "content": prompt_usuario})

    # Envia a mensagem para a sessão de chat da API e exibe a resposta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                resposta = st.session_state.chat_session.send_message(prompt_usuario)
                texto_resposta = resposta.text.strip()
                
                st.write(texto_resposta)
                
                # Salva a resposta da IA no histórico local da tela
                st.session_state.historico_mensagens.append({"role": "assistant", "content": texto_resposta})

            except Exception as e:
                st.error(f"Erro ao gerar resposta: {e}")