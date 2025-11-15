temp = float(input('Digite a temperatura em Celsius: '))

contadora = 0
soma = 0

while temp != -273:
    soma += temp
    contadora += 1
    temp = float(input('Digite a temperatura em Celsius: '))

media = soma / contadora
print(f'A média das temperaturas digitadas é: {media}°C')
