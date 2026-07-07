import os
from google import genai


MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")

tema_usuario = input("Sobre qual assunto você quer gerar um resumo de 3 linhas? " )
