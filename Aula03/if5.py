prod1 = float(input("Digite o preço do primeiro produto: R$ "))
prod2 = float(input("Digite o preço do segundo produto: R$ "))
prod3 = float(input("Digite o preço do terceiro produto: R$ "))

if prod1 <= prod2 and prod1 <= prod3:
    barato = prod1
    nome = "primeiro produto"
elif prod2 <= prod1 and prod2 <= prod3:
    barato = prod2
    nome = "segundo produto"
else:
    barato = prod3
    nome = "terceiro produto"

print(f"O {nome} é o mais barato, custando R$ {barato:.2f}.")