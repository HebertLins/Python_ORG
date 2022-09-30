A = int(input("Digite um número inteiro: "))
B = int(input("Digite outro número inteiro: "))

for i in range(A,B+1):
    if i % 2 == 0 and i > 10:
        print(i)