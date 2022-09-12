n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 == n2 == n3:
    print('Os 3 valores são iguais')
else:
    if n1==n2 or n1==n3 or n2==n3:
        print('Dois valores são iguias')
        if n1 == n2 and n1 > n3:
            print(f'O primeiro valor {(n1)} e o segundo {(n2)} são iguais e maiores que o terceiro {(n3)}')
        elif n2 == n3 and n2 > n1:
            print(f'O segundo valor {(n2)} e o terceiro {(n3)} são iguais e maiores que o primeiro {(n1)}')
        elif n1 == n3 and n1 > n2:
            print(f'O primeiro valor {(n1)} e o terceiro {(n3)} são iguais e maiores que o segundo {(n3)}')
        else:
            if n1 > n2 and n1 > n3:
                print(f'O primeiro valor é o maior {(n1)}')
            elif n2 > n1 and n2 > n3:
                print(f'O segundo valor é o maior {(n2)}')
            else:
                print(f'O terceiro valor é o maior {(n3)}')