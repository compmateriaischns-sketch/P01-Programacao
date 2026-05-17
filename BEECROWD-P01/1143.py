n = int(input("Quantidade de linhas de saída: "))
a, b, c, cont = 1, 1, 1, 1
for i in range(1, n+1, 1):
    a, b, c = i, i*cont, i*cont*cont
    print(f'{a} {b} {c}')
    cont += 1