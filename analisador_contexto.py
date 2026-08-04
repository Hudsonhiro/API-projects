import os
from xmlrpc import client
from google import genai
from google.genai import types

def responder_com_contexto():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    caminho_manual = "manual_escola.txt"
    try:
        with open(caminho_manual, "r", encoding="utf-8") as arquivo:
            conteudo_manual = arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo '{caminho_manual}' não encontrado. Certifique-se de que o arquivo existe.")
        return
    
    regras_do_sistema = f"""
    Você é um assistente de atendimento virtual da Escola Primavera.
    Sua única fonte de verdade é o Manual de Diretrizes fornecido abaixo.
    Se a resposta para a pergunta do usuário não estiver no manual, responda educadamente: 
    "Infelizmente não tenho essa informação no meu manual interno. Por favor, contate a secretaria."

    --- MANUAL DE DIRETRIZES ---
    {conteudo_manual}
    ---------------------------
    """

    print("--- ASSISTENTE VIRTUAL COM CONTEXTO (Manual da Escola) ---")
    pergunta_usuario = input("\nDigite a pergunta do usuário: ");

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta_usuario,
            config=types.GenerateContentConfig(
                system_instruction=regras_do_sistema,
                temperature=0.2 
            )
        )

        print("\n💬 [Resposta do Assistente]:")
        print(response.text.strip())

    except Exception as e:
        print(f"Erro ao processar consulta: {e}")

if __name__ == "__main__":
    responder_com_contexto()