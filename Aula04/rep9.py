votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_brancos = 0

for i in range(0, 20):
    voto = int(input("Informe o seu voto (1-4 para candidatos, 5 para nulo, 6 para branco): "))
    
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Voto inválido. Por favor, informe um número entre 1 e 6.")
print("Resultado da eleição:")
print(f'Votos do candidato 1: {votos_candidato1}')
print(f'Votos do candidato 2: {votos_candidato2}')
print(f'Votos do candidato 3: {votos_candidato3}')
print(f'Votos do candidato 4: {votos_candidato4}')
print(f'Votos nulos: {votos_nulos}')
print(f'Votos em branco: {votos_brancos}')
print(f'Percentual de votos nulos: {(votos_nulos / 20) * 100}%')
print(f'Percentual de votos em branco: {(votos_brancos / 20) * 100}%')
print('Votação Encerrada')