import os
from google import genai
from google.genai import types

def gerar_resposta_limitada():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    print("--- RESUMIDOR EXPRESSO (CONTROLE DE TOKENS) ---")
    texto_longo = input("\nCole um texto ou faça uma pergunta complexa: ")

    try:
        # Aumentamos o limite para 150 tokens (espaço suficiente para 2 ou 3 frases completas)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=texto_longo,
            config=types.GenerateContentConfig(
                system_instruction="Você é um assistente ultra-sintético. Responda de forma direta e sem rodeios.",
                temperature=0.2,
                max_output_tokens=300, # 👈 Limite seguro para não estourar no meio de uma frase
                thinking_config=types.ThinkingConfig(thinking_budget=0)
                
            )
        )

        # Checagem de segurança: garantimos que response.text não é None antes de formatar
        if response.text:
            print("\n⚡ [Resposta Rápida Limitada]:")
            print(response.text.strip())
        else:
            print("\n⚠️ A resposta foi interrompida antes de ser gerada. Tente aumentar o max_output_tokens.")

    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    gerar_resposta_limitada()