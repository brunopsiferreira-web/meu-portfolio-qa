import json

def validar_resposta_api(resposta: dict) -> bool:
    """Valida se a resposta da API tem os campos obrigatórios."""
    campos_obrigatorios = ["id", "nome", "status"]
    return all(campo in resposta for campo in campos_obrigatorios) and resposta["status"] == "ativo"

if __name__ == "__main__":
    # Simulando resposta de uma API real
    resposta_simulada = {
        "id": 1,
        "nome": "Produto A",
        "preco": 29.99,
        "status": "ativo"
    }

    print("🔍 Validando resposta da API...")
    if validar_resposta_api(resposta_simulada):
        print("✅ Teste PASSOU: Resposta válida!")
        
        # Salvar em JSON
        with open('resposta_api.json', 'w', encoding='utf-8') as arquivo:
            json.dump(resposta_simulada, arquivo, indent=4, ensure_ascii=False)
        print("💾 Resposta salva em 'resposta_api.json'")
    else:
        print("❌ Teste FALHOU: Resposta inválida!")