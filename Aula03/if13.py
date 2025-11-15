venda_2022 = float(input("Digite a quantidade total de vendas em 2022: "))
venda_2023 = float(input("Digite a quantidade total de vendas em 2023: "))

var_percentual = 100 * (venda_2023 - venda_2022) / (venda_2022)

if var_percentual > 20:
    print(f'Bonificação para o time de vendas: {var_percentual:.2f}%')

elif var_percentual <= 2 and var_percentual <= 20:
    print(f'Pequena bonificação para time de vendas: {var_percentual:.2f}%')

elif var_percentual <= 20 and var_percentual >= -10:
    print('Planejamento de políticas de incentivo às vendas: {var_percentual:.2f}%')
else:
    print('Corte de gastos')