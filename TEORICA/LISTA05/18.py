import random

v = [[random.randint(0,9) for i in range(15)]for j in range(15)]

for i in range(15):
    for j in range(15):
        if j == 0:
                print('[', end =' ')
        print(v[i][j], end = ' ')
        if j == 14:
                print(end = ']\n')

# for linha in v:
#     print(linha)