n = str(input("Digite o seu nome: "))
ec = str(input("Digite o seu estado civil(Casada ou Solteira): "))
s = str(input("Digite o seu sexo (M ou F): "))

if (s.upper == 'F' and ec.upper == 'CASADA'):
    tc = str(input("Por quantos anos você é casada?: "))
    print(f"Você é uma MULHER CASADA faz {tc} anos e seu nome é {n}.")
else:
    print("Você não se encaixa no perfil.")
