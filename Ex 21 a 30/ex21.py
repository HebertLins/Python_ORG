n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

op = int(input("""Digite um valor correspondente a operação que deseja realizar
1 - Multiplicação
2 - Adição
3 - Divisão
4 - Subtração
5 - Finalizar o programa
Qual operação deseja?: """))

if (op == 1) :
    r = n1 * n2
    print (f"O resultado da operação é {r:.2f}")
elif (op == 2):
    r = n1 + n2
    print (f"O resultado da operação é {r:.2f}")
elif (op == 3):
    if (n1 == 0 or n2 == 0):
        print("ERRO!")
    else:
        r = n1 / n2
    print (f"O resultado da operação é {r:.2f}")
elif (op == 4):
    r = n1 - n2
    print (f"O resultado da operação é {r:.2f}")
elif (op == 5):
    print("Programa encerrado!")
else:
    print("O valor que você digitou não corresponde as opções.")