pEmail = []
email = []
pSenha = []
senha = []
con = 0

#Cadastro simulador de banco#
for i in range (0,2,1):
    pEm = str(input("Email: "))
    pEmail.append(pEm)
    pSe = str(input("Senha: "))
    pSenha.append(pSe)
    print()
print("==============================")

for a in range (0,2,1):
    print("LOGIN")
    em = str(input("Email: "))
    email.append(em)
    se = str(input("Senha: "))
    senha.append(se)
    print()
    con = 0

    for c in range (0,2,1):
        if (em == pEmail[c] and se == pSenha[c]):
            print("Login realizado com sucesso!")
            con = con + 1
            print("==============================")
            print()
        elif (con == 0):
            print("Por favor realize o seu cadastro")
            em = str(input("Email: "))
            email.append(a)
            se = str(input("Senha: "))
            senha.append(a)
            con = con + 1
