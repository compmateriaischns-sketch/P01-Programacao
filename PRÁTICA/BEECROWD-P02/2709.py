while True:
    try:
        m = int(input())
        v = [int(input()) for i in range(m)]
        n = int(input())
            

        k = m
        soma = 0

        for i in range(m-1,-1,-n):
            soma = soma + v[i]

        p = 0
        for i in range(1,soma+1):
            if (soma%i) == 0:
                p += 1
        if p == 2:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')

    except EOFError:
        break
