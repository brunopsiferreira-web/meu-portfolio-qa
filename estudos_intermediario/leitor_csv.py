import csv
import os

def ler_usuarios_csv(caminho_arquivo: str):
    """Lê um arquivo CSV e imprime os e-mails dos usuários."""
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado!")
        return

    with open(caminho_arquivo, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        print("📧 E-mails para teste:")
        for linha in leitor:
            print(f'- O nome do usuário é {linha['nome']}, o e-mail é {linha['email']} e a senha é {linha['senha']} ')
           
            
if __name__ == "__main__":
    # Caminho relativo ao script
    diretorio = os.path.dirname(__file__)
    caminho = os.path.join(diretorio, 'usuarios.csv')
    ler_usuarios_csv(caminho)