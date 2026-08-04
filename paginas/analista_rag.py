import os
import streamlit as st
from google import genai
from google.genai import types

st.title("📄 Analista de Documentos (RAG)")
st.write("Faça upload de um arquivo `.txt` para conversar com o contexto do documento.")

@st.cache_resource
def iniciar_cliente():
    # Tenta buscar das Secrets do Streamlit Cloud; se não achar, busca das variáveis de ambiente locais
    chave = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    return genai.Client(api_key=chave)

client = iniciar_cliente()

with st.sidebar:
    st.header("📂 Documento")
    arquivo = st.file_uploader("Escolha um arquivo .txt", type=["txt"])
    conteudo = ""
    if arquivo is not None:
        conteudo = arquivo.read().decode("utf-8")
        st.success("Documento carregado!")

if "hist_rag" not in st.session_state:
    st.session_state.hist_rag = []

for msg in st.session_state.hist_rag:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Pergunte algo sobre o documento...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.hist_rag.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Analisando..."):
            try:
                prompt_completo = f"CONTEXTO:\n{conteudo}\n\nPERGUNTA: {prompt}" if conteudo else prompt
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt_completo,
                    config=types.GenerateContentConfig(
                        temperature=0.2,
                        thinking_config=types.ThinkingConfig(thinking_budget=0)
                    )
                )
                texto = response.text.strip()
                st.write(texto)
                st.session_state.hist_rag.append({"role": "assistant", "content": texto})
            except Exception as e:
                st.error(f"Erro: {e}")