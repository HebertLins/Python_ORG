nome = []
idade = []
sexo = []


for c in range (0,100,1):
    n = str(input("Digite um nome: "))
    nome.append(n)

    i = int(input("Digite uma idade: "))
    while (i < 0):
        print("Valor inválido!")
        i = int(input("Digite uma idade: "))
    idade.append(i)

    s = str(input("Digite o seu sexo(M ou F): ")).upper()
    while (s != "M" and s != "F"):
        print("Valor inválido!")
        s = str(input("Digite o seu sexo(F ou M): ")).upper()
    sexo.append(s)   

    print()

print("Pessoas acima de 18")
print()

for i in range (0,100,1):
    if (idade[i] >= 18):
        print("Nome: {}, Idade: {}, Sexo: {}".format(nome[i], idade[i], sexo[i]))