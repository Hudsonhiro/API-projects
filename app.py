import streamlit as st

# 1. Definir as Páginas
pagina_chat = st.Page("paginas/chat.py", title="Chat Conversacional", icon="💬", default=True)
pagina_rag = st.Page("paginas/analista_rag.py", title="Analista de Documentos", icon="📄")
pagina_json = st.Page("paginas/extrator_json.py", title="Extrator JSON", icon="📊")

# 2. Configurar a Navegação Lateral
pg = st.navigation(
    {
        "Aplicações de IA": [pagina_chat, pagina_rag, pagina_json]
    }
)

# 3. Configuração Global da Página
st.set_page_config(
    page_title="Gemini AI Engineering Hub",
    page_icon="🤖",
    layout="centered"
)

# 4. Executar a Página Selecionada
pg.run()