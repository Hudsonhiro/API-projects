import os
from google import genai
from google.genai import types

def classificador_problema():
    MINHA_CHAVE = "AQ.Ab8RN6KjonvuE8yfEMN8UpPoFTZGPiLBwjnhO_F4SKjmnbCzeA"
    client = genai.Client(api_key=MINHA_CHAVE)

    historico_exemplos = [
        types.Content(role="user", parts=[types.Part.from_text("Meu monitor está com uma mancha preta e piscando")]),
        types.Content(role="model", parts=[types.Part.from_text("CATEGORIA: HARDWARE")]),
        
        types.Content(role="user", parts=[types.Part.from_text("Não consigo instalar o Office, dá erro de licença")]),
        types.Content(role="model", parts=[types.Part.from_text("CATEGORIA: SOFTWARE")]),
        
        types.Content(role="user", parts=[types.Part.from_text("O Wi-fi não conecta no segundo andar da casa")]),
        types.Content(role="model", parts=[types.Part.from_text("CATEGORIA: REDE")]),
    ]

    print("=== Classificador de Problemas de TI ===")
    problema_usuario = input("Descreva o problema que você está enfrentando: ")

    try:
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="Você é um triador de suporte técnico. Responda apenas com a categoria.",
                history=historico_exemplos,
            )
        )

        response = chat.send_message(problema_usuario)

    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API: {e}")
        return
    
if __name__ == "__main__":
    classificador_problema()