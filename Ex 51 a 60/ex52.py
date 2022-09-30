numeros = []
n1 = 0
for c in range(0,10,1):
    n = int(input("Digite um valor: "))
    numeros.append(n)
    if (n > n1):
        nm = n
        n1 = n
print("O maior valor digitado foi: {}".format(nm))
