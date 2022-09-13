print("Digite um valor positivo")
n = int(input("Digite um valor: "))
while n < 0:
    print("Valor inválido!")
    n = int(input("Digite um valor: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
print("O fatorial de", n, "é", fatorial)

print("Deseja uma nova execução? (S/N))")
resposta = input()
if resposta == "S":
    print("Digite um valor positivo")
    n = int(input("Digite um valor: "))
    while n < 0:
        print("Valor inválido!")
        n = int(input("Digite um valor: "))
    fatorial = 1
    for i in range(1, n + 1):
        fatorial = fatorial * i
    print("O fatorial de", n, "é", fatorial)
else:
    print("Fim do programa")