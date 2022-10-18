num = [20]
contI = 0
contP = 0

for c in range(0,4,1):
    n = int(input("Digite um valor: "))
    num.append(n)

for c in range(0,4,1):
    resto = num[c] % 2
    if (resto == 0):
        contP = contP + 1
    else:
        contI = contI + 1

contG = contP + contI
porcenP = (contP * 100) / contG
porcenI = (contI * 100) / contG

print("A quantidade de valores pares foi   {}".format(contP))
print("A porcentagem de valores pares foi   {:.1f}%".format(porcenP))
print("A quantidade de valores ímpares foi {}".format(contI))
print("A porcentagem de valores ímpares foi   {:.1f}%".format(porcenI))