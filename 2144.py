i = 0
soma = 0
while True:
    w1, w2, r = map(int, input().split(' '))
    m1 = w1 * (1 + (r/30))
    m2 = w2 * (1 + (r/30))
    m = (m1 + m2)/2
    soma = soma + m
    if m >= 1 and m < 13:
        print('Nao vai da nao')
    elif m >= 13 and m < 14:
        print('E 13')
    elif m >= 14 and m < 40:
        print('Bora, hora do show! BIIR!')
    elif m >= 40 and m <= 60:
        print('Ta saindo da jaula o monstro!')
    elif m > 60:
        print('AQUI E BODYBUILDER!!')
    elif w1 == 0 and w2 == 0 and r == 0:
        break
    i += 1

if soma/i > 40:
    print('', end = '\n')
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')