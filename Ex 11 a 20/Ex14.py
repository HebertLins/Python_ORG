a = float(input('Informe a sua altura: '))
p = float(input('Informe o seu peso: '))
IMC = p/(a*a)
if IMC < 19:
    print('Você está muito magro')
elif IMC >= 19 and IMC < 24:
    print('Você está com o seu peso adequado')
else:
    print('Você está acima do peso')

