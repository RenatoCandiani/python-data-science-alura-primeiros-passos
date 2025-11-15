inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

if inicio < fim:
    for i in range(inicio, fim + 1):
        print(i)
elif inicio > fim:
    for i in range(fim + 1, inicio):
        print(i)
else:
    print("Os valores são iguais; não há intervalo para exibir.")