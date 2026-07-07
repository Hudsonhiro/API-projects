import os
from google import genai
from google.genai import types

def testar_criatividade():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    prompt = "Escreva um título de três palavras para um post sobre aprender programação."

    print("--- TESTANDO CONFIGURAÇÕES DE TEMPERATURA ---")

    try:
        resposta_tecnica = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.0,
            )
        )
        print("Resposta com temperatura 0.0 (mais técnica):")
        print(resposta_tecnica.text)
        resposta_creativa = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=1.0,
            )
        )
        print("Resposta com temperatura 1.0 (mais criativa):")
        print(resposta_creativa.text)   
    except Exception as e:
        print(f"Erro ao gerar conteúdo: {e}")

if __name__ == "__main__":
    testar_criatividade()