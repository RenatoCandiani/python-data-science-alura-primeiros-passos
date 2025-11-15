num = int(input("Digite um número inteiro entre 1 e 10: "))

print(f'Tabuada do número {num}: ')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}' )