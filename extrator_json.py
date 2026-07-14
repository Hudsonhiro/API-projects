import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# 1. Definimos o contrato de dados que a escola precisa
class FichaMatricula(BaseModel):
    aluno_nome: str = Field(description="Nome completo do aluno encontrado no texto.")
    aluno_idade: int = Field(description="Idade do aluno apenas em números inteiros.")
    serie_desejada: str = Field(description="A série ou ano escolar que o responsável solicita.")

def extrair_dados_profissionais():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    # 2. No System Instruction, mantemos os exemplos (Few-Shot), mas agora em formato JSON!
    regras_e_exemplos = """
    Você é um extrator de dados escolares de alta precisão.
    Sua função é ler e-mails de pais e preencher a ficha de matrícula obrigatoriamente no formato JSON solicitado.
    
    --- EXEMPLO 1 ---
    Input: "Gostaria de saber se tem vaga para o Pedro Henrique de 8 anos no 3º ano."
    Output: {"aluno_nome": "Pedro Henrique", "aluno_idade": 8, "serie_desejada": "3º ano"}
    
    --- EXEMPLO 2 ---
    Input: "Quero matricular a Julia Silveira, ela tem 15 anos e vai para o 1º ano do médio."
    Output: {"aluno_nome": "Julia Silveira", "aluno_idade": 15, "serie_desejada": "1º ano do Ensino Médio"}
    """

    print("--- EXTRATOR DE MATRÍCULAS EM SINAL DE MERCADO (JSON) ---")
    email_recebido = input("\nCole o texto do e-mail: ")

    try:
        # 3. Fazemos a chamada travando a saída em JSON estruturado
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=email_recebido,
            config=types.GenerateContentConfig(
                system_instruction=regras_e_exemplos,
                temperature=0.0,
                response_mime_type="application/json",
                response_schema=FichaMatricula # Força o cumprimento das regras do Pydantic
            )
        )

        # 4. Convertendo o texto puro do JSON em um dicionário Python real
        dados_finais = json.loads(response.text)

        print("\n✅ [JSON Gerado e Validado com Sucesso]:")
        print(json.dumps(dados_finais, indent=4, ensure_ascii=False))

        # 5. Simulando o que faríamos para salvar no banco de dados:
        print("\n🚀 [Simulação de Banco de Dados]:")
        print(f"Salvando no banco de dados da escola -> Nome: {dados_finais['aluno_nome']} | Idade: {dados_finais['aluno_idade']}")

    except Exception as e:
        print(f"Erro no processamento dos dados: {e}")

if __name__ == "__main__":
    extrair_dados_profissionais()