vetor = []
i_maior, i_menor = 0, 0
for i in range(5):
    v = int(input("Digite o elemento do vetor: "))
    vetor.append(v)
    if i == 0:
        maior = v
        menor = v
        continue
    
    if v > maior:
        i_maior = i
        maior = v 
    if v < menor:
        i_menor = i
        menor = v

print('As posições são:' '\n' f'Maior: {i_maior} | Menor: {i_menor}')