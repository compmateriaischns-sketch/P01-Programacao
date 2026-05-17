I, F = input().split()

I = int(I)
F = int(F)

if I > F:
    tempo = 24 - I + F
    print(f'O JOGO DUROU {tempo} HORA(S)')
elif F > I:
        tempo = F - I
        print(f'O JOGO DUROU {tempo} HORA(S)')
else:
    print('O JOGO DUROU 24 HORA(S)')