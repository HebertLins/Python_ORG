from calendar import c


n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))

s = n1 + n2

if (s < n3):
    print("A soma dos primeiros dois valores ({}) é menor que o terceiro ({}).".format(s,n3))
else:
    print("A soma dos primeiros dois valores ({}) é maior que o terceiro ({}).".format(s,n3))