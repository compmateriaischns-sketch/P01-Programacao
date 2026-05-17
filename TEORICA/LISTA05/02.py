vetor = []
for i in range(20):
    v = int(input("Digite o elemento do vetor: "))
    vetor.append(v)
    if i == 0:
        maior = v
        menor = v
        continue
    
    if v > maior:
        maior = v 
    if v < menor:
        menor = v

print(f'Maior: {maior} | Menor: {menor}')