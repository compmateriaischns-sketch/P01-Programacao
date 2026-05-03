h = int(input("Valor H inicial: "))
if h == 0:
    pass
else:
    v = h
    i = 0
    s = [v]
    m = h
    while v != 1:
        if v % 2 == 0:
            v2 = (1/2)*v
            v2 = int(v2)
        else:
            v2 = 3*v + 1
            v2 = int(v2)
        s.append(v2)
        print(v2)
        v = v2
        for i in range(len(s)):
            if s[i] > m:
                m = s[i]
    print(*s)
    print(f'O maior número é: {m:.0f}')
