colonia_a = 4
colonia_b = 10

taxa1 = 0.3
taxa2 = 0.15

dias = 0

while colonia_a <= colonia_b:
    colonia_a += 1 + taxa1
    colonia_b += 1 + taxa2
    dias += 1

print(f"Levará {dias} dias para a colonia A ultrapassar a colônia B")