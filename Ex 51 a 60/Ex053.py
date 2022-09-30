from ast import If
from collections import abc


numeros = []
for c in range (0,20,1):
    n = int(input("Digite um valor ({}): ".format(c)))
    numeros.append(n)

for i in range (0,20,1):
    if (i < 19): 
        n2 = numeros[i] * numeros[i+1]
        numeros[i] = n2

for i in range (0,20,1):
    print(numeros[i])
