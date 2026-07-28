# 🤖 Gemini AI Engineering Hub

Uma suíte completa de aplicações e técnicas de **Engenharia de IA** e integração com **LLMs**, utilizando a SDK oficial da **Google GenAI** e interface gráfica interativa em **Streamlit**.

![Streamlit Web App](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/Model-Gemini%202.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## 🎯 Funcionalidades Implementadas

- **Aplicações Web Interativas (`app.py`):** Interface para atendimento rápido integrada ao Gemini via Streamlit.
- **Gestão Eficiente de Tokens (`resumidor_curto.py`):** Controle fino de `max_output_tokens` e otimização com `thinking_budget=0` para respostas rápidas e sem cortes.
- **Sessões e Memória Contínua (`chat_memoria.py`):** Implementação de chat com histórico usando `client.chats.create()`.
- **RAG & Contexto Estático:** Injeção dinâmica e leitura otimizada de documentos para mitigar alucinações.
- **Saídas Estruturadas (Structured Outputs):** Respostas em formato estrito de JSON validado via Pydantic.
- **Engenharia de Prompt:** Aplicação prática de *System Instructions* e *Few-Shot Prompting*.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Frontend:** Streamlit
* **SDK LLM:** `google-genai` (Google GenAI SDK)
* **Ambiente Linux/WSL:** Ubuntu no WSL2

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone [https://github.com/Hudsonhiro/gemini-ai-engineering-hub.git](https://github.com/Hudsonhiro/gemini-ai-engineering-hub.git)
cd gemini-ai-engineering-hub
