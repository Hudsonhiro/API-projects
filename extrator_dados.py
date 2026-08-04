import os
from google import genai
from google.genai import types

def extrair_dados_matricula():
    
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    regras_e_exemplos = """
    Você é um assistente de secretaria escolar especializado em extração de dados brutos.
    Sua função é ler um e-mail informal e extrair: Nome do Aluno, Idade e Série.
    
    Responda SEMPRE seguindo estritamente o formato dos exemplos abaixo:
    
    --- EXEMPLO 1 ---
    Input: "Olá, gostaria de saber se tem vaga para o meu filho Pedro Henrique. Ele fez 8 anos em janeiro e queríamos colocá-lo no 3º ano."
    Output: ALUNO: Pedro Henrique | IDADE: 8 anos | SÉRIE: 3º ano
    
    --- EXEMPLO 2 ---
    Input: "Boa tarde, me chamo Mariana e quero matricular a Julia Silveira na escola. Ela tem 15 anos e vai cursar o 1º ano do ensino médio."
    Output: ALUNO: Julia Silveira | IDADE: 15 anos | SÉRIE: 1º ano do Ensino Médio
    
    --- EXEMPLO 3 ---
    Input: "Vaga para o Lucas Rezende, ele está saindo da escola antiga com 6 anos para entrar no 1º ano do fundamental."
    Output: ALUNO: Lucas Rezende | IDADE: 6 anos | SÉRIE: 1º ano do Ensino Fundamental
    """

    print("=== Extrator de Dados de Matrícula ===")
    email_recebido = input("Digite o conteúdo do e-mail recebido: ")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=email_recebido,
            config=types.GenerateContentConfig(
                system_instruction=regras_e_exemplos,
                temperature=0.0,
            )
        )

        print("Dados extraídos com sucesso:")
        print(response.text)
    except Exception as e:
        print("Ocorreu um erro ao extrair os dados:", str(e))

if __name__ == "__main__":
    extrair_dados_matricula()