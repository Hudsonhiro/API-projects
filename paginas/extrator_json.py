import os
import json
import streamlit as st
import pandas as pd
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

st.title("📊 Extrator de Dados JSON")
st.write("Extraia informações de relatos para tabelas e estruturas JSON estritas.")

@st.cache_resource
def iniciar_cliente():
    # Tenta buscar das Secrets do Streamlit Cloud; se não achar, busca das variáveis de ambiente locais
    chave = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    return genai.Client(api_key=chave)

client = iniciar_cliente()

class FeedbackCliente(BaseModel):
    nome_cliente: str = Field(description="Nome do cliente ou 'Não informado'")
    sentimento: str = Field(description="Positivo, Neutro ou Negativo")
    categoria: str = Field(description="Suporte Técnico, Financeiro, Reclamação ou Elogio")
    urgencia: str = Field(description="Alta, Média ou Baixa")
    resumo_problema: str = Field(description="Resumo do relato em uma frase")

texto_input = st.text_area("Relato do Cliente:", height=150)

if st.button("Extrair Dados", type="primary"):
    if texto_input.strip():
        with st.spinner("Processando..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Extraia os dados: {texto_input}",
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=FeedbackCliente,
                        temperature=0.1,
                        thinking_config=types.ThinkingConfig(thinking_budget=0)
                    )
                )
                dados = json.loads(response.text)
                st.success("Concluído!")
                st.dataframe(pd.DataFrame([dados]), use_container_width=True)
                with st.expander("Ver JSON Puro"):
                    st.json(dados)
            except Exception as e:
                st.error(f"Erro: {e}")