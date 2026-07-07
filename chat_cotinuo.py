import os
from google import genai

MINHA_CHAVE = "AQ.Ab8RN6KjonvuE8yfEMN8UpPoFTZGPiLBwjnhO_F4SKjmnbCzeA"
client = genai.Client(api_key=MINHA_CHAVE)

chat = client.chats.create(model="gemini-2.5-flash")

print("O seu chat inteligente 1.0 está pronto para uso!")
print("Digite 'sair' para encerrar o chat.")

while True:
    pergunta = input("Tu: ")

    if pergunta.lower() == "sair":
        print("Encerrando o chat. Até logo!")
        break

    resposta = chat.send_message(pergunta)
    print(f"IA: {resposta.text}")