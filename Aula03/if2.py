percent = float((input("Digite o percentual de crescimento: ")))

if percent > 0:
    print("Houve um crescimento.")
elif percent < 0:
    print("Houve uma diminuição.")
else:
    print("Não houve variação.")