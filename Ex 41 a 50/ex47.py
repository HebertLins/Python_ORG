resp = "S"
while (resp == "S"):
    n = int(input("Digite o valor que você deseja: "))

    while (n < 0):
        print("Valor inválido!")
        n = int(input("Digite o valor que você deseja: "))
    
    fat = n
    c = n

    while(c > 1): 
        c = c - 1 
        n = fat
        fat = n * c
        print("{} x {} = {}".format(n,c,fat))
    resp = (input("Você deseja continuar (S/N)? ")).upper