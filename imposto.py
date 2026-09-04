import os
os.system("cls")

def somaImposto(taxaImposto, custo):
    preco_final = custo * (1 + taxaImposto / 100)
    return preco_final


print("=== Cálculo de Preço com Imposto ===")

taxa = float(input("Digite a taxa de imposto (%): "))
custo = float(input("Digite o custo do item (antes do imposto): "))

preco = somaImposto(taxa, custo)

print(f"\nPreço final com imposto: R$ {preco:.2f}")
