numeros = []
resp = "S"
erro = 0

max = int(input("Digite a quantidade de valores: "))
if (max > 20 or max < 0):
    print("VALOR INVÁLIDO!")
    max = int(input("Digite a quantidade de valores: "))

for c in range(0,max,1):
    n = int(input("Digite um valor: "))
    numeros.append(n)

while (resp == "S"):
    np = int(input("Digite o valor que deseja saber a sua posição: "))

    for c in range(0,max,1):
        if (numeros[c] == np):
            print("O valor está na posição: {}".format(c))
        else:
            erro = erro + 1

    if erro == max:
        print("Valor não existe!")

    resp = str(input("Você deseja consultar outro valor (S/N)? "))
