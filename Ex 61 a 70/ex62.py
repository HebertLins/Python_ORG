num = []
v = []
s = []
name = []
cont = 0

for c in range (0,5,1):
    nome = input("Nome: ")
    name.append(nome) 
    sexo = input("Sexo (M ou F): ")
    s.append(sexo)
    idade = int(input("Idade: "))
    num.append(idade)
    v.append(idade)

for c in range (0,5,1):

    for i in range (0,5,1):
        if (num[c] > num[i]):
            cont = cont + 1

    v[cont] = num[c]
    cont = 0

print() 
print("==_= LISTA DE PESSOAS EM ORDEM DECRESCENTE (idade) =_==")

for c in range (4,-1,-1):
    print("Nome:", name[c])
    print("Idade:", v[c])
    print("Sexo:", s[c])
    print()