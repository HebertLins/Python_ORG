numeros = []
for c in range (0,10,1):
    n = int(input("Digite um valor ({}): ".format(c)))
    numeros.append(n)

maior = numeros[0]
for i in range (0,10,1):
    if (numeros[i] > maior):
        maior = numeros[i]

print("O maior valor digitado foi: {}".format(maior))
