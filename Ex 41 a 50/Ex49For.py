print("Soma de todos os valores")

n1 = int(input("Digite o numero inicial: "))
n2 = int(input("Digite o numero final: "))
soma = 0

for i in range(n1,n2+1):
    soma += i

print("A soma dos numeros do intervalo e: ", soma)