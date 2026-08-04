# 🤖 Gemini AI Engineering Hub

Plataforma de aplicações web com IA generativa construída com Python, Streamlit e o SDK oficial da Google GenAI (`google-genai`).

🌐 **Acesse a aplicação online:** [https://seu-app.streamlit.app](https://seu-app.streamlit.app) *(substitua pelo seu link real)*

---

## 🛠️ Arquiteturas Implementadas

1. **💬 Chat Conversacional:** Memória persistente da sessão usando `st.session_state` e `client.chats.create`.
2. **📄 Analista de Documentos (RAG):** Leitura de arquivos `.txt` com injeção estática de contexto para respostas baseadas no documento.
3. **📊 Extrator de Dados JSON:** Saídas estruturadas com Pydantic (`BaseModel`, `Field`) e exibição de dados em DataFrame interativo do Pandas.

## 🚀 Como Executar Localmente

```bash
# Clonar o repositório
git clone [https://github.com/Hudsonhiro/API-projects.git](https://github.com/Hudsonhiro/API-projects.git)

# Acessar a pasta e criar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar a chave de API e rodar o app
export GEMINI_API_KEY="SUA_CHAVE_AQUI"
streamlit run app.py