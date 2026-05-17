import random
matriz = [[random.randint(1, 100) for i in range(6)] for j in range(3)]

print('Matriz (impressão direta): \n', matriz)

print("Matriz impressão correta: ")
for linha in matriz:
    print(linha)

print("Elementos da primeira coluna: ")
for linha in matriz:
    print(linha[0])

print("Elementos da coluna 5 e soma: ")
soma = 0
for i in range(3):
    print(matriz[i][5])
    soma = soma + matriz[i][5]

print("Soma dos elementos da última coluna 5: ", soma)