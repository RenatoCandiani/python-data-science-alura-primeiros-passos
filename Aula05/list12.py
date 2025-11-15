votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

total_votos = 0
vencedor = ''
maior_numero_votos = 0

for design, voto_desing in votos.items():
    total_votos += voto_desing

    if voto_desing > maior_numero_votos:
        maior_numero_votos = voto_desing
        vencedor = design

porcentagem_vencedor = 100 * (maior_numero_votos / total_votos)

print(f'{vencedor} venceu: ')
print(f'Porcentagem de votos: {porcentagem_vencedor:.2f}%')