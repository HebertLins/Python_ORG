n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
if n1 == n2:
    print(f'Os dois valores são iguais, representam o número: {(n1)}')
elif n1 > n2:
    print(f'O primeiro valor ({n1}) é MAIOR que o primeiro ({n2})')
else:
    print(f'O segundo valor ({n2}) é MAIOR que o primeiro ({n1})')