n = int(input("Digite a quantidade de valores que você deseja: "))
s1 = 2
somador = 3
soma = 0

while (n < 0 or n > 50):
    print("Valor inválido!")
    n = int(input("Digite a quantidade de valores que você deseja: "))

print(s1)

for i in range(0, n - 1):
    n = n - 1
    s2 = s1 + somador
    somador = somador + 2
    print(s2)
    s1 = s2
    soma = soma + s2 