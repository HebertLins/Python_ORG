a = float(input("Informe os valores da aceleração: "))
v0 = float(input("Informe a velocidade inicial: "))
t = float(input("Informe o tempo de percurso: "))

V = v0 + (a * t)

#Km = V * 3.6

print(f"O veículo está à {V}Km/H")

if ( V < 40 ):
    print("Muito Lento!")
elif (40 < V <= 60):
    print("Velocidade permitida")
elif ( 60 < V <= 80 ):
    print("Velocidade de cruzeiro")
elif (80 < V <= 120 ):
    print("Alta velocidade")
else:
    print("Velocidade muito rápida!")