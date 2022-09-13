n = int(input("Digite a quantidade de valores que você deseja: "))
s1 = 2
somador = 3
soma = 0
c = 1
exp = 3

while (n < 0 or n > 50):
    print("Valor inválido!")
    n = int(input("Digite a quantidade de valores que você deseja: "))


print(s1)

while (n > 0):
    n = n - 1
    c = c + 1
    s2 = s1 + somador
    somador = somador + 2
    s1 = s2
    soma = soma + s2 
    cexp = c**exp
    print("{}/{}".format(s2,cexp))



