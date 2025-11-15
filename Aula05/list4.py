lista_numeros = []

for i in range(0, 5):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

print(f"Números digitados: {lista_numeros[::-1]}")