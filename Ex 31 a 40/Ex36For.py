v = int(input("Digite um valor positivo: "))

while (v < 0):
    print("O valor deve ser positivo.")
    v = int(input("Digite um valor positivo: "))

ct = int(input("Digite o começo da tabuada: "))
tt = int(input("Digite o final da tabuada: "))

while (ct > tt):
    print("O começo deve ser maior que o final.")
    tt = int(input("Digite o final da tabuada: "))

for i in range(tt, ct, -1):
    r = v * i
    print(f"{v} * {i} = {r}")