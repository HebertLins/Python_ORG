print("O primeiro valor deve ser maior que 10 e menor que o segundo")
n1 = int(input("Digite um intervalo inteiro (A): "))
n2 = int(input("Digite um intervalo inteiro (B): "))

c = n1

while (n1 < 0 or n2 < 0 or n1 < 10):
    print("O primeiro valor deve ser maior que 10 e menor que o segundo")
    n1 = int(input("Digite um intervalo inteiro (A): "))
    n2 = int(input("Digite um intervalo inteiro (B): "))

n2 = n2 - 1

while (c < n2):
    c = c + 1
    vrf = c % 2
    if (vrf == 0):
        print(c)