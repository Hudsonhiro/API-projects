import os
from google import genai

AP_KEY = os.getenv("GENAQ.Ab8RN6KL7n_VK6GZWTFbnuHVSu8edhSKtThfEd7OnHnpMXkQ0w")
client = genai.Client(api_key=AP_KEY)

tema_usuario = input("Sobre qual assunto você quer gerar um resumo de 3 linhas? " )
