import os

from google import genai
from google.genai import types

def gerar_email():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    print("=== Formatador de E-mails inteligentes===")

    nome_destinatario = input("Digite o nome do destinatário: ")
    motivo = input("Digite o motivo do e-mail: ")
    tom = input("Digite o tom do e-mail (ex: formal, informal, amigável): ")

    usuario_mensagem = f""" Gerar um e-mail com as seguintes especificações:
    - Destinatário: {nome_destinatario}
    - Motivo Principal: {motivo}
    - Tom da escrita: {tom}
    """

    instrucao_sistema = """ Você é um assistente executivo especializado em comunicação corporativa escrita. Sua única tarefa é escrever e-maisls perfeitos com base nos dados fornecidos pelo usuário.

    Regras estritas:
    - Respeite rigososamente o tom solicitado pelo usuário.
    - Inclua espaços reservados para preenchimento posteior entre colchetes, como [Sua Assunatura] ou [Data], se necessário.
    - Não adicione comentários antes ou depois do e-mail. Devolva Apenas o texto do e-mail pronto para copiar e colar. """

    print("\nFormatando seu e-mail corporativo... Aguarde. \n")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=usuario_mensagem,
            config=types.GenerateContentConfig(
                system_instruction=instrucao_sistema,
                temperature=0.2,
            )
        )

        print("=" * 50)
        print(response.text)
        print("=" * 50)

    except Exception as e:
        print("Ocorreu um erro ao gerar o e-mail:", str(e))

if __name__ == "__main__":
    gerar_email()
