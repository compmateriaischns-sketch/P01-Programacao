teste = True
while teste:
    n = int(input("Digite o numero de rodadas: "))
    if 0 <= n <= 10:
        pa = 0
        pb = 0
        i = 0
        while i < n:
            a, b = map(int, input("N1 N2: ").split())
            i += 1
            if 0 <= a <= 10 and 0 <= b <= 10:
                if a > b:
                    pa +=1
                elif b > a:
                    pb += 1
            else: 
                print("Valores entre 0 e 10. Repita!")
                i -= 1    
        teste = False
        if n == 0:
            pass
        else:
            print(f'{pa} {pb}')
    else:
        print("N precisa estar entre 0 e 10.")
        continue

    