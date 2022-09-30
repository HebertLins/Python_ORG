numeros = []
for c in range(9,-1,-1):
    n = int(input("Digite um valor: "))
    numeros.append(n)

print("Os valores digitados (em ordem decrescente) foram: ")

for c in range(9,-1,-1):
    print(numeros[c])