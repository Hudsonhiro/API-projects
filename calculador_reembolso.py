import os
import json
from google import genai
from pydantic import BaseModel, Field

class RespostaReembolso (BaseModel):
    raciocinio: str = Field(description="Explicação passo a passo da aplicação das regras de negócio")
    valor_reembolso: str= Field(description="O valor final ou percentual a ser devolvido.")

def calcular_reembolso():
    MINHA_CHAVE = os.environ.get("GEMINI_API_KEY", "SUA_CHAVE_AQUI")
    client = genai.Client(api_key=MINHA_CHAVE)

    print("--- Sistema de Análise de Reembolso ---")
    pedido = input("Descreva o pedido de reembolso, incluindo detalhes relevantes: ")

    instrucao = """
    Você é um auditor de reembolsos de uma companhia aérea.
    Antes de dar o valor final, você deve analisar as regras no campo 'raciocinio'.
    Regras:
    - Antecedência > 48h: 100%
    - Antecedência 24h-48h: 50%
    - Antecedência < 24h: 0%
    - Motivo 'Saúde': Sempre 100%
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pedido,
            config={
                "response_mime_type": "application/json",
                "response_schema": RespostaReembolso,
                "system_instruction": instrucao
            }
        )

        resultado = json.loads(response.text)
        print("\n--- Resultado da Análise ---")
        print(f"Raciocínio: {resultado['raciocinio']}")
        print(f"Valor do Reembolso: {resultado['valor_reembolso']}")

    except Exception as e:
        print(f"Erro ao gerar conteúdo: {e}")

if __name__ == "__main__":
    calcular_reembolso()