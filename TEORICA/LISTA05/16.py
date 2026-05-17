"""6. Considere uma matriz de valores de notas de atletas numa olimpíadas em que cada 
linha representa um atleta e cada coluna a nota de um jurado. Considerando uma 
matriz de 10 atletas e 5 jurados, preencha a matriz com valores fornecidos pelo 
usuário e imprima na tela qual o atleta que teve a maior soma de notas entre os 
jurados (Imprima a posição da linha do atleta) """

notas = [[float(input(f"Digite a nota {j+1} do atleta {i+1}: ")) for j in range(2)] for i in range(3)]
print(notas)

for i in range(3):
    soma = 0
    for j in range(2):
        # print(notas[i][j])
        soma  += notas[i][j]
    print(f'A soma das notas do atleta {i+1} é {soma}.')
    if i == 0:
        maior = soma
        k = i+1
        continue
    if soma > maior:
        maior = soma
        k = i+1

print(f'O atleta com a maior nota está na linha {k} e sua nota foi {maior:.2f}')

"""Digite a nota 1 do atleta 1: 1
Digite a nota 2 do atleta 1: 1
Digite a nota 1 do atleta 2: 2
Digite a nota 2 do atleta 2: 2
Digite a nota 1 do atleta 3: 3
Digite a nota 2 do atleta 3: 3
[[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
1.0
1.0
A soma das notas do atleta 1 é 2.0.
2.0
2.0
A soma das notas do atleta 2 é 4.0.
3.0
3.0
A soma das notas do atleta 3 é 6.0.
O atleta com a maior nota está na linha 3 e sua nota foi 6.00"""