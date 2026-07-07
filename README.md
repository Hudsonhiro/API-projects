# Moderador de Comentários Inteligente com Gemini API

Este é um sistema autônomo em Python que atua como moderador de conteúdo para e-commerce, filtrando comentários ofensivos antes de serem publicados.

## 🚀 Tecnologias Utilizadas
* Python 3
* Google GenAI SDK (Modelo: `gemini-2.5-flash`)
* Ambiente Linux via WSL

## 💡 Conceitos Aplicados
* **System Instructions:** Isolamento de regras do sistema contra ataques de prompt injection.
* **Deterministic Output:** Configuração de `temperature=0.0` para garantir consistência nas respostas (`APROVADO` / `REPROVADO`).
* **Resiliência:** Tratamento de exceções com blocos `try/except` para falhas de rede.

## 🛠️ Como Rodar
1. Configure sua chave do Gemini nas variáveis de ambiente:
   ```bash
   export GEMINI_API_KEY="sua_chave_aqui"