a = float(input('Informe a sua altura: '))
p = float(input('Informe o seu peso(KG): '))
s = str(input("Informe o seu sexo(M ou F): "))
IMC = p/(a*a)

F = str

if (s == F):
    if (IMC < 19):
        print('Você está muito magro')
    elif (IMC >= 19 and IMC < 24):
        print('Você está com o seu peso adequado')
    else:
        print('Você está acima do peso')
else:
    if (IMC < 20):
        print('Você está muito magro')
    elif (IMC >= 20 and IMC < 25):
        print('Você está com o seu peso adequado')
    else:
        print('Você está acima do peso')
