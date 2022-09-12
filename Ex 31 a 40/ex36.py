x = int(input("Digite um valor: "))
while x < 0:
    print("Valor inválido, digite um número positivo!")
    n1 = int(input("Digite um valor: "))

a = int(input("Digite um valor (A): "))
b = int(input("Digite um valor (B): "))

while ( a >= b ):
    print("Os valores digitados são inválidos")
    b = int(input("Digite um valor (B): "))

for c in range (b,a-1,-1):
    t = x * c
    print("{} x {} = {}".format(x,c,t))