import os
from google import genai

def gerar_resumo():
    # 1. Inicializa o cliente (ele busca automaticamente a variável GEMINI_API_KEY)
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    print("=== Gerador de Resumos IA ===")
    
    # 2. Pede o tema para o usuário no terminal
    tema = input("Digite o tema que você deseja resumir: ")
    
    if not tema.strip():
        print("O tema não pode ser vazio!")
        return

    print("\nProcessando seu resumo... Aguarde.\n")

    # 3. Monta o prompt garantindo a restrição de 3 linhas
    prompt = f"Escreva um resumo sobre '{tema}'. O resumo deve ter OBRIGATORIAMENTE exatamente 3 linhas."

    try:
        # 4. Faz a requisição para a API
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # 5. Exibe o resultado
        print("-" * 40)
        print(response.text)
        print("-" * 40)

    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API: {e}")

if __name__ == "__main__":
    gerar_resumo()