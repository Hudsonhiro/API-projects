import streamlit as st
import os
from google import genai
from google.genai import types

# 1. Configuração da página do navegador (Título da aba e ícone)
st.set_page_config(
    page_title="Assistente de Atendimento",
    page_icon="🤖",
    layout="centered"
)

# 2. Elementos Visuais na Tela
st.title("🤖 Assistente de Atendimento com IA")
st.write("Digite sua dúvida abaixo e nossa IA responderá instantaneamente de forma resumida!")

# Campo de texto para o usuário digitar
pergunta_usuario = st.text_input("Sua dúvida:", placeholder="Ex: Qual é o horário de atendimento?")

# Botão de envio
if st.button("Perguntar à IA", type="primary"):
    if not pergunta_usuario:
        st.warning("Por favor, digite uma pergunta antes de clicar no botão!")
    else:
        # Mostra um indicador visual de carregamento enquanto a IA pensa
        with st.spinner("Processando resposta..."):
            try:
                MINHA_CHAVE = os.environ.get("GEMINI_API_KEY")
                client = genai.Client(api_key=MINHA_CHAVE)

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=pergunta_usuario,
                    config=types.GenerateContentConfig(
                        system_instruction="Você é um assistente virtual atencioso. Responda em no máximo 2 frases.",
                        temperature=0.3,
                        max_output_tokens=300,
                        thinking_config=types.ThinkingConfig(thinking_budget=0)
                    )
                )

                # Exibe o resultado dentro de um cartão de sucesso na tela web
                st.success("Resposta gerada!")
                st.write(response.text.strip())

            except Exception as e:
                st.error(f"Erro ao conectar com a IA: {e}")