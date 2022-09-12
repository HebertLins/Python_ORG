p = float(input("Informe o valor do produto: R$"))
op = int(input("""Código Condição de pagamento
1 	À vista em dinheiro ou cheque, recebe 10% de desconto
2 	À vista no cartão de crédito, recebe 15% de desconto
3 	Em duas vezes, preço normal de etiqueta sem juros
4 	Em quatro vezes, preço normal de etiqueta mais juros de 10%
Escolha a sua opção: """))

if (op == 1):
    d = p*10/100
    pd = p - d
    print(f"Dessa forma, o valor a ser pago será R${pd:.2f}.")
if (op == 2):
    d = p*15/100
    pd = p - d
    print(f"Dessa forma, o valor a ser pago será R${pd:.2f}.")
if (op == 3):
    par = p / 2
    print(f"Dessa forma, o valor será pago em 2x sem juros, a primeira parcela será de R${par:.2f}")
if (op == 4):
    d = p*10/100
    pd = p + d
    par = pd / 4
    print(f"Dessa forma, o valor será pago em 4x com juros de 10%, a primeira parcela será de R${par:.2f}")
else:
    print("A opção que você escolheu não existe!")
