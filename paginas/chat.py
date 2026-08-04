import os
import streamlit as st
from google import genai
from google.genai import types

st.title("💬 Chatbot com Memória")
st.write("Converse em tempo real com o Gemini mantendo o contexto da sessão.")

@st.cache_resource
def iniciar_cliente():
    return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

client = iniciar_cliente()

if "historico_mensagens" not in st.session_state:
    st.session_state.historico_mensagens = []

if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Você é um assistente virtual prestativo, claro e objetivo.",
            temperature=0.3
        )
    )

for mensagem in st.session_state.historico_mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

prompt_usuario = st.chat_input("Digite sua mensagem...")

if prompt_usuario:
    with st.chat_message("user"):
        st.write(prompt_usuario)
    st.session_state.historico_mensagens.append({"role": "user", "content": prompt_usuario})

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                resposta = st.session_state.chat_session.send_message(prompt_usuario)
                texto = resposta.text.strip()
                st.write(texto)
                st.session_state.historico_mensagens.append({"role": "assistant", "content": texto})
            except Exception as e:
                st.error(f"Erro: {e}")