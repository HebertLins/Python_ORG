n = float(input("Digite um valor: "))

if (n < 0):
    nm = n * 3 
    print(f"O número digitado era negativo, portanto ele foi multiplicado por 3X, resultando em: {nm:.2f}")
else:
    nm = n * 2
    print(f"O número digitado era positivo, portanto ele foi multiplicado por 2X, resultando em: {nm:.2f}")