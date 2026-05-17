arquivo_matriz = "matriz.txt"
matriz_int = []
print("Matriz lida do arquivo:\n", end='\n ')
with open(arquivo_matriz, "r") as file:
    for line in file:
        a = [int(x) for x in line.split()]
        matriz_int.append(a)
        print(line, end=' ')  # Imprime cada linha lida do arquivo

# print(matriz_int)        

# a) Todos os elementos, exceto os elementos da diagonal principal.
print("\n\nElementos da matriz, exceto os da diagonal principal: \n", end='\n ')
for i in range(10):
    for j in range(10):
        if j == 9:
            print("\n", end=' ')
        if i != j:
            print(matriz_int[i][j], end=' ')

print("\nElementos abaixo da diagonal principal: ")
for i in range(10):
    for j in range(10):
        if i > j:
            print(f'{matriz_int[i][j]} ', end=' ')
        if i == j:
            print("\n", end=' ') 

print("\nA soma de cada linha da matriz: \n", end='\n ')
for i in range(10):
    soma = 0
    for j in range(10):
        soma = soma + matriz_int[i][j]
    print(f'Soma da linha {i}: {soma}', end='\n ')
   
print("\nO produto de cada coluna da matriz é: \n", end ='\n ')
for i in range(10):
    prod = 1
    for j in range(10):
        prod = prod*matriz_int[j][i]
    print(f"Produto da coluna {i}: {prod}", end = '\n ')