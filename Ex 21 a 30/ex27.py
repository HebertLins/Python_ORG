n = int(input("Digite um valor: "))

d = n % 2

if (d == 1):
    print("O valor digitado é ÍMPAR")
    ns = n + 8
    print(f"O valor é {n} + 8 = {ns}")
else:
    print("O valor digitado é PAR")
    ns = n + 5
    print(f"O valor é {n} + 5 = {ns}")