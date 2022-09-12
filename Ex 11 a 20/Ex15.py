n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print ('Esse valores formam um triângulo')
    if n1 == n2 == n3:
        print ('Esse é um triângulo equilátero')
    if n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 != n1:
        print ('Esse é um triângulo isósceles')
    if n1 != n2 != n3:
        print ('Esse é um triângulo escaleno')
else:
    print ('Esses valores não formar um triângulo')
