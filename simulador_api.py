# simulador_api.py

import json

# Simulando resposta de uma API de produtos
resposta_api_1 = {
    "id": 1,
    "nome": "Pão de sal",
    "preco": 5.99,
    "status": "ativo"
}

resposta_api_2 = {
    "id": 2,
    "nome": "Pão de queijo",
    "preco": 3.99,
    "status": "ativo"
}

# Validação: o produto está ativo?
if resposta_api_1["status"] == "ativo":
    print("✅ Teste de status: PASS")
else:
    print("❌ Teste de status: FAIL")
    
if resposta_api_2["status"] == "ativo":
    print("✅ Teste de status: PASS")
else:
    print("❌ Teste de status: FAIL")
    

# Salvar resposta em arquivo JSON (útil para relatórios)
with open('resposta_api.json', 'w') as f:
    json.dump(resposta_api_1, f, indent=4)

print("Resposta salva em 'resposta_api.json'")