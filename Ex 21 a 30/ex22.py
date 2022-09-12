from re import L


op = int(input("""Digite um valor correspondente a operação que deseja realizar
1 – Triângulo
2 – Quadrado
3 – Retângulo
4 – Círculo
5 – Fim de processo
Qual operação deseja?: """))

if (op == 1) :
    b = float(input("Informe o valor da Base: "))
    h = float(input("Informe o valor da Altura:  "))
    a = b * (h*h)
    print (f"A área desse triângulo é {a:.2f}cm²")
elif (op == 2):
    l = float(input("Informe o valor do Lado:"))
    a = l*l
    print (f"A área desse quadrado é {a:.2f}cm²")
elif (op == 3):
    b = float(input("Informe o valor da Base: "))
    h = float(input("Informe o valor da Altura:  "))
    a = b * h
    print (f"A área desse retângulo é {a:.2f}cm²")
elif (op == 4):
    raio = float(input("Informe o valor da Raio: "))
    a = 3.14 * (raio*raio)
    print (f"A área desse círculo é {a:.2f}cm²")
elif (op == 5):
    print("Programa encerrado!")
else:
    print("O valor que você digitou não corresponde as opções.")