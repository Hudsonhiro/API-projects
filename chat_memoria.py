import os
from google import genai
from google.genai import types

def iniciar_chat_com_memoria():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    # 1. Definimos a personalidade do assistente no System Instruction
    regras = "Você é um assistente pessoal amigável, atencioso e com excelente memória."

    # 2. Criamos a sessão de CHAT (O nosso "Bloco de Notas" automático)
    # Usamos o modelo rápido gemini-2.5-flash
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=regras,
            temperature=0.7 # Um pouco mais de criatividade para uma conversa fluida
        )
    )

    print("--- CHATBOT COM MEMÓRIA PERSISTENTE ---")
    print("(Digite 'sair' a qualquer momento para encerrar)\n")

    # 3. O Loop de conversa contínua
    while True:
        mensagem_usuario = input("Você: ")

        if mensagem_usuario.lower() == "sair":
            print("\nAssistente: Até logo! Foi um prazer conversar com você.")
            break

        try:
            # Enviamos a mensagem através do objeto 'chat' (ele anota o histórico sozinho!)
            response = chat.send_message(mensagem_usuario)
            
            print(f"\nAssistente: {response.text.strip()}\n")

        except Exception as e:
            print(f"\nErro de conexão: {e}\n")

if __name__ == "__main__":
    iniciar_chat_com_memoria()