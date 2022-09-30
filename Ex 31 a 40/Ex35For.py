v = int(input("Digite um valor positivo: "))

while (v < 0):
    print("O valor precisa ser positivo.")
    v = int(input("Digite um valor positivo: "))

for i in range(1, 11, 1):
    r = v * i
    print(f"{v} * {i} = {r}")