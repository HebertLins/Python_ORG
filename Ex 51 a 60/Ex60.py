num = []
v = []
cont = 0

for c in range (0,5,1):
    n = int(input("Digite um número: "))
    num.append(n)
    v.append(n)

for c in range (0,5,1):

    for i in range (0,5,1):
        if (num[c] > num[i]):
            cont = cont + 1

    v[cont] = num[c]
    cont = 0

for c in range (0,5,1):
    print(v[c])
