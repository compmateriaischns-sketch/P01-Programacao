soma = 1
for i in range(1, 21, 1):
    S = (i*2 + 1)/(2**i)
    soma = S + soma
    # print(soma)

print(f'{soma:.2f}')