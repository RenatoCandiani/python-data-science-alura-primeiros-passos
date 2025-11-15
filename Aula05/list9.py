respostas = []

gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0

for i in range(0, 10):
    resposta = input(f'Digite a resposta da {i+1}° questão (A-B-C-D-E): ').upper()
    respostas.append(resposta)

for i in range(0, 10):
    if respostas[i] == gabarito[i]:
        nota += 1

print(f'Nota Final: {nota}')