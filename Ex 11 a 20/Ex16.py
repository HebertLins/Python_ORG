h = float(input("Informe o valor da hipotenusa: "))
c1 = float(input("Informe o valor de um cateto: "))
c2 = float(input("Informe o valor do outro cateto: "))

h2 = h*h
sc = (c1*c1) + (c2+c2)

if (sc == h2):
    print("Esse é um triângulo retângulo!")
else :
    print("Esse não é um triângulo retângulo")