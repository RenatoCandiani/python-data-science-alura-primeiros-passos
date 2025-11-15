num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f'O resultado da adição é: {resultado}')
elif operacao == '-':
    resultado = num1 - num2
    print(f'O resultado da subtração é: {resultado}')
elif operacao == '*':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é: {resultado}')
elif operacao == '/':
    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')
else:
    print("Operação inválida!")
    resultado = 0
    
if resultado % 2 == 0:
    print("O resultado é um número par.")
else:
    print("O resultado é um número ímpar.")

if resultado % 1 == 0:
    print("O resultado é um número inteiro.")
else:
    print("O resultado é um número decimal.")

if resultado >= 0:
    print("O resultado é um número positivo.")
else:
    print("O resultado é um número negativo.")