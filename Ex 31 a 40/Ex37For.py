print("Tabuada de 1 a 20")

for tabuada in range (1, 21, 1):
    for x in range (1, 11, 1):
        r = tabuada * x
        print(f"{tabuada} X {x} = {r}")
    input("Pressione um botão...")