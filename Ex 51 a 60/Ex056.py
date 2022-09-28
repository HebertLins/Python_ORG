nome = []
idade = []

for c in range (0,5,1):
    n = str(input("Digite um nome: "))
    nome.append(n)
    i = str(input("Digite uma idade: "))
    idade.append(i)

for i in range (0,5,1):
    print()
    print("O nome é {} e a idade é {}".format(nome[i],idade[i]))
    