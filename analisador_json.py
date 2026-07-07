import os
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class AnaliseFeedback(BaseModel):
    sentimento: Literal["positivo", "negativo"] = Field(
        description="O sentimento geral do texto fornecido."
    )
    assunto_principal: str = Field(
        description="Um resumo de até 3 palavras sobre o assunto principal do texto."
    )

def analisar_texto():
    MINHA_CHAVE = "AQ.Ab8RN6KjonvuE8yfEMN8UpPoFTZGPiLBwjnhO_F4SKjmnbCzeA"
    client = genai.Client(api_key=MINHA_CHAVE)

    print("=== Analisador de Sentimentos IA ===")

    texto_cliente = """
    Olha, o produto de vocês chegou no prazo e a embalagem estava linda, parabéns. 
    Mas na hora que eu fui ligar, ele simplesmente não funcionou! Ficou apitando e soltou um cheiro estranho. 
    Tentei falar com o suporte e ninguém me atendeu até agora. Estou muito frustrado porque precisava disso para trabalhar hoje.
    """

    print("Enviando texto confuso para análise estruturada... Aguarde.\n")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Analise o seguinte feedback: {texto_cliente}",
            config={
                "response_mime_type": "application/json",
                "response_schema": AnaliseFeedback,
            }
        )

        print("\n--- Resposta bruta da API (JSON PURO) ---")
        print(response.text)
        print("-----------------------------------------------\n")

        import json
        dados_convertidos = json.loads(response.text)

        print(f"O Python leu com sucesso!")
        print(f"Sentimento detectado: {dados_convertidos['sentimento'].upper()}")
        print(f"Assunto principal: {dados_convertidos['assunto_principal']}")

    except Exception as e:
        print(f"Erro ao analisar o texto: {e}")

if __name__ == "__main__":
    analisar_texto()