import requests

def test_get_api():
    """Testa a listagem de usuários."""
    response = requests.get("https://www.freepublicapis.com/api/random")
    assert response.status_code == 200, f"Esperado 200, obtido {response.status_code}"
    data = response.json()
    assert "emoji" in data, "Chave 'data' não encontrada na resposta"
    assert "health" in data, "Chave 'data' não encontrada na resposta"
    assert len(data["emoji"]) > 0, "Nenhum emoji encontrado"
    assert int(data["health"]) > 0, "Nenhum healt encontrado"
    
    print("✅ GET /geral - PASS")
    print(data['emoji'])
    print(data['health'])

if __name__ == "__main__":
    try:
        test_get_api()
        # test_create_user()
        print("\n🎉 Todos os testes de API passaram!")
    except Exception as e:
        print(f"\n❌ Falha nos testes: {e}")