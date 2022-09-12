p1 = float(input('Informe o valor do primeiro produto: '))
p2 = float(input('Informe o valor do segundo produto: '))
p3 = float(input('Informe o valor do terceiro produto: '))
p4 = float(input('Informe o valor do quarto produto: '))
p5 = float(input('Informe o valor do quinto produto: '))
t = p1+p2+p3+p4+p5
pag = float(input('Informe o valor do pagamento: '))
troco = pag - t
print('O valor do troco é R${:.2f}'.format(troco))