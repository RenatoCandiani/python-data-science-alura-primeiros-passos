num = int(input("Informe um número inteiro: "))

e_primo = True

if num <= 1:
    e_primo = False
else:
    for i in range (2, num):
        if num % i == 0:
            e_primo = False
            break

if e_primo:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')