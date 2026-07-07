import os
from google import genai

def gerar_resumo():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")

    client = genai.Client(api_key=MINHA_CHAVE)

    print("=== Gerador de Resumos IA ===")

    tema = input("Digite o tema que você deseja resumir: ")
    if not tema.strip():
        print("O tema não pode ser vazio!")
        return
    print("\nProcessando seu resumo... Aguarde.\n")

    prompt = f"Escreva um resumo sobre '{tema}'. O resumo deve ter OBRIGATORIAMENTE exatamente 3 linhas."

    try:
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        print("-" * 40)
        print(response.text)
        print("-" * 40)

    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API: {e}")


if __name__ == "__main__":
    gerar_resumo()      

    print("\nResumo gerado com sucesso! Obrigado por usar o Gerador de Resumos IA.")