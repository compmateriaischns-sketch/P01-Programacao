import random

matriz = [[random.randint(1,100) for i in range(10)] for j in range(10)]
matriz_nova = []
for i in range(10):
    #for j in range(10):
        # if j == 9:
        #     print(end = '\n ')
    print(matriz[i])

# for i in range(10):
#     for j in range(10):
#         matriz_nova[i][j] = matriz[i][j]
linha2 = []
coluna8 = []
for i in range(10):
    a = matriz[2][i]
    b = matriz[i][8]
    linha2.append(a)
    coluna8.append(b)

print('\nLinha a serem trocadas: ', end = '')
print(end = '\n')
print(linha2)
print(coluna8)
print(end = '\n')

for i in range(10):
    matriz[i][8] = linha2[i]
    matriz[2][i] = coluna8[i]
# matriz[1][4] = coluna8[2]
# matriz[4][1] = linha2[4]

print("Matriz nova invertida", end = '\n')

for i in range(10):
    print(matriz[i])

        