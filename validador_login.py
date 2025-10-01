# validador_login.py

def validar_login(usuario, senha):
    """Valida se o usuário e senha estão corretos."""
    if usuario == "standard_user" and senha == "secret_sauce":
        return True
    else:
        return False

# Testes
print("Teste 1 - Credenciais válidas:")
resultado1 = validar_login("standard_user", "secret_sauce")
print("Resultado:", "Pass" if resultado1 else "Fail")

print("\nTeste 2 - Credenciais inválidas:")
resultado2 = validar_login("user_errado", "senha_errada")
print("Resultado:", "Pass" if not resultado2 else "Fail")