def validar_login(usuario: str, senha: str) -> bool:
    """
    Valida se as credenciais correspondem a um usuário autorizado.
    Coloca-se em dict o login e a senha do usuário.
    """
    credenciais_validas = {
        "standard_user": "secret_sauce",
        "admin": "admin123"
    }
    return credenciais_validas.get(usuario) == senha

# Testes
if __name__ == "__main__":
    print("Teste 1 - Credenciais válidas:")
    print("Resultado:", "PASS" if validar_login("standard_user", "secret_sauce") else "FAIL")

    print("\nTeste 2 - Credenciais inválidas:")
    print("Resultado:", "PASS" if not validar_login("hacker", "123") else "FAIL")