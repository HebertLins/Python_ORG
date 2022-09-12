print("Digite 3 valores distindos")
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if (n1 == n2 or n1 == n3 or n2 == n3):
    print("Existem valores iguais")
    if (n1 == n2 == n3):
        print("Os 3 valores são iguais")
else:
    if(n1 > n2 and n1 > n3 and n2 > n3):
        print(n3,n2,n1)
    if(n1 > n2 and n1 > n3 and n3 > n2):
        print(n2,n3,n1)
    if(n2 > n1 and n2 > n3 and n1 > n3):
        print(n3,n1,n2)
    if(n2 > n1 and n2 > n3 and n3 > n1):
        print(n1,n3,n2)
    if(n3 > n1 and n3 > n2 and n2 > n1):
        print(n1,n2,n3)
    if(n3 > n1 and n3 > n2 and n1 > n2):
        print(n2,n1,n3)