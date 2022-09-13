n = int(input("Digite um valor para N: "))
while(n <= 0 or n >= 50):
    print("Valor inválido!")
    n = int(input("Digite um valor para N: "))
soma = 0
for i in range(1, n + 1):
    print(i, "/", i + 1)
    soma = soma + i / (i + 1)
print("A soma dos N primeiros valores é: ", soma)