n = int(input("Digite a quantidade de valores que você deseja: "))
s1 = 1
somador = 2
soma = 0

while (n < 0 or n > 50):
    print("Valor inválido!")
    n = int(input("Digite a quantidade de valores que você deseja: "))

while (n > 0):
    n = n - 1
    s2 = s1 / somador
    s1 = s1 + 1
    somador = somador + 1
    print("{:.2f}".format(s2))
    soma = soma + s2 
print("A soma dos valores da sequência é igual a: {:.2f}".format(soma))
    