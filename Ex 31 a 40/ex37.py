c1 = 0
c2 = 0
while (c1 < 20):
    c1 = c1 + 1
    while (c2 < 10):
        c2 = c2 + 1
        c3 = c1 * c2
        print("{} x {} = {}".format(c1, c2, c3))
    c2 = 1
    input("Pressione ENTER para continuar: ")