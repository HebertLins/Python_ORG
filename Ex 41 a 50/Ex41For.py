n = int(input("Digite um valor para N: "))
while(n <= 0 or n >= 100):
    print("Valor inválido!")
    n = int(input("Digite um valor para N: "))
a = 2
b = 5
c = 10
d = 17
soma = 0
for i in range(1, n + 1):
    print(a, b, c, d)
    soma = soma + a + b + c + d
    a = a + 1
    b = b + 2
    c = c + 3
    d = d + 4
print("A soma dos N primeiros valores é: ", soma)