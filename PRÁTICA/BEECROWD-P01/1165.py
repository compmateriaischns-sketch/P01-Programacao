n = int(input("Quantos testes: "))

while n > 0:
    num = int(input("Digite um número: "))
    cont = 0
    i = 1
    for i in range(1, num+1, 1):
        if (num % i) == 0:
            cont +=1
    n -= 1
    if cont == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')