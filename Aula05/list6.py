dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if mes == 2:
    if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
        dias_fevereiro = 29
    else:
        dias_fevereiro = 28

    if dia >= 1 and dia <= dias_fevereiro:
        print(f"A data {dia}/{mes}/{ano} é válida.")
    else:
        print(f"A data {dia}/{mes}/{ano} é inválida.")

elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia >= 1 and dia <= 31:
        print(f"A data {dia}/{mes}/{ano} é válida.")
    else:
        print(f"A data {dia}/{mes}/{ano} é inválida.")

elif mes in [4, 6, 9, 11]:
    if dia >= 1 and dia <= 30:
        print(f"A data {dia}/{mes}/{ano} é válida.")
    else:
        print(f"A data {dia}/{mes}/{ano} é inválida.")

else:
    print(f"A data {dia}/{mes}/{ano} é inválida.")