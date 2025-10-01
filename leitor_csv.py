# leitor_csv.py

import csv

print("Lendo massa de dados para testes...")

with open('usuarios.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"- Testando login para: {linha['email']}")