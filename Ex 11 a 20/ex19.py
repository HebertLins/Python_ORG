c1 = float(input("Informe a nota do C1: "))
c2 = float(input("Informe a nota do C2: "))

sc = c1 + c2
m = sc/2

print(f"A média do aluno é {m}")

if (m >= 5 ):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")