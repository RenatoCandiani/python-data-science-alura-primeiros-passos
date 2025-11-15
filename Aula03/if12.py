quantidade_litros = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível  (E para etanol e D para diesel)': ").upper()

if tipo_combustivel == 'E':
    preco_por_litro = 1.70
    if quantidade_litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04

elif tipo_combustivel == 'D':
    preco_por_litro = 2.00
    if quantidade_litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05

else:
    print("Tipo de combustível inválido!")
    preco_por_litro = 0
    desconto = 0

preco_total = quantidade_litros * preco_por_litro
valor_desconto = preco_total * desconto
preco_final = preco_total - valor_desconto  
print(f'O preço final a ser pago é: R$ {preco_final:.2f}')