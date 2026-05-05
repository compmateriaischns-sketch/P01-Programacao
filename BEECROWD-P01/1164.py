N = int(input())

for i in range (N):
    X = int(input())
    a=1
    soma=0
    while a < X:
        if X%a == 0:
            soma = soma + a
        a += 1
    if soma == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')