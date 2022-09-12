n1 = int(input("Digite um valor: "))
c = 0

while n1 < 0:
    print("Valor inválido, digite um número positivo!")
    n1 = int(input("Digite um valor: "))

while c < 5:
    c = c + 1
    print("{} x {} = {}".format(n1,c,n1 * c))