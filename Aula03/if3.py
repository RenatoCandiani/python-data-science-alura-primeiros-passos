letra = str(input("Digite uma letra: ")).lower()
vogais = "aeiou"

if letra in vogais:
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")