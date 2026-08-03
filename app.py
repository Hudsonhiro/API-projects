import os
import json
import streamlit as st
import pandas as pd
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# 1. Configuração da página
st.set_page_config(
    page_title="Extrator Estruturado JSON",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Extrator de Dados Estruturados com IA")
st.write("Digite ou cole um relato/feedback de cliente abaixo para extrair dados em formato **JSON estrito** e visualizá-los em tabela.")

# 2. Inicialização da API do Gemini
@st.cache_resource
def iniciar_cliente():
    minha_chave = os.environ.get("GEMINI_API_KEY")
    return genai.Client(api_key=minha_chave)

client = iniciar_cliente()

# 3. Definição do Esquema Pydantic (Garantia de tipo e estrutura)
class FeedbackCliente(BaseModel):
    nome_cliente: str = Field(description="Nome do cliente mencionado no texto, ou 'Não informado' se não houver.")
    sentimento: str = Field(description="Sentimento geral do texto: Positivo, Neutro ou Negativo.")
    categoria: str = Field(description="Categoria do feedback: Suporte Técnico, Financeiro, Reclamação de Produto ou Elogio.")
    urgencia: str = Field(description="Nível de urgência da demanda: Alta, Média ou Baixa.")
    resumo_problema: str = Field(description="Um resumo sucinto em uma frase sobre o relato do cliente.")

# 4. Campo de entrada de texto
texto_input = st.text_area(
    "Relato do Cliente:",
    height=150,
    placeholder="Ex: Olá, meu nome é Carlos. Estou muito chateado pois cobravam um valor indevido na minha fatura deste mês. Preciso disso resolvido urgente!"
)

# 5. Processamento e Exibição de Resultados
if st.button("Analisa e Extrair Dados (JSON)", type="primary"):
    if not texto_input.strip():
        st.warning("Por favor, digite algum texto antes de analisar.")
    else:
        with st.spinner("Extraindo e estruturando dados..."):
            try:
                # Chamada com Structured Outputs estrito
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Extraia as informações do seguinte relato: {texto_input}",
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=FeedbackCliente,
                        temperature=0.1, # Temperatura baixa para máxima precisão
                        thinking_config=types.ThinkingConfig(thinking_budget=0)
                    )
                )

                # Converter a string JSON retornada para um dicionário Python
                dados_json = json.loads(response.text)

                st.success("Dados extraídos com sucesso!")

                # Exibição 1: Tabela Visual amigável
                st.subheader("📋 Tabela de Dados Extraídos")
                df = pd.DataFrame([dados_json])
                st.dataframe(df, use_container_width=True)

                # Exibição 2: Estrutura JSON pura (ideal para desenvolvedores/APIs)
                with st.expander("🔍 Ver JSON Puro (Raw Data)"):
                    st.json(dados_json)

            except Exception as e:
                st.error(f"Erro ao processar estruturação: {e}")
