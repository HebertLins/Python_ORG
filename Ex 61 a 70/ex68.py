matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for l in range (0,3,1):
    for c in range (0,4,1):
        matriz[l][c] = int(input("Digite um valor: "))

cnst = int(input("Insira uma Constante multiplicativa: "))

for l in range (0,3,1):
    for c in range (0,4,1):
        matriz2[l][c] = matriz[l][c] * cnst

for i in range (0,3,1):
    print(matriz[i])

print()

for i in range (0,3,1):
    print(matriz2[i])