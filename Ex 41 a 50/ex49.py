from stringprep import in_table_a1


i = int(input("Digite um valor: "))
f = int(input("Digite outro valor: "))

i1 = i
f1 = f
soma = 0

while (i > f):
    print("O segundo valor deve ser maior que o primeiro!")
    i = int(input("Digite um valor: "))
    f = int(input("Digite outro valor: "))

while (i <= f):
    i = i + 1
    soma = soma + i
print("A soma dos valores entre {} e {} é igual a: {}".format(i1,f1,soma))