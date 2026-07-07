import os
from google import genai
from google.genai import types

def analisar_comentario():
    # Nota: Lembre-se de usar sua chave real localmente, aqui vou deixar um padrão seguro.
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    regras_do_moderador = """Você é um moderador de comentários estrito. 
    Analise o texto enviado. Se contiver ofensas, xingamentos ou baixaria, responda APENAS com 'REPROVADO'. 
    Se o comentário for limpo e adequado, responda APENAS com 'APROVADO'."""

    print("--- SISTEMA DE MODERAÇÃO DE COMENTÁRIOS CONTINUO ---")
    print("(Digite 'sair' para encerrar o programa)\n")

    # O loop mantém o programa vivo para testar vários comentários seguidos
    while True:
        comentario = input("\nDigite o comentário para análise: ")

        # Condição de saída do programa
        if comentario.lower() == "sair":
            print("Encerrando o sistema de moderação.")
            break

        if not comentario.strip():
            print("Comentário vazio. Tente novamente.")
            continue

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=comentario,
                config=types.GenerateContentConfig(
                    system_instruction=regras_do_moderador,
                    temperature=0.0,
                )
            )

            # Lógica de validação
            if "REPROVADO" in response.text.upper():
                print("❌ Alerta: Este comentário viola as diretrizes e foi deletado.")
            else:
                print("✅ Sucesso: O comentário foi publicado no site.")

        except Exception as e:
            print(f"Erro ao analisar comentário: {e}")

if __name__ == "__main__":
    analisar_comentario()