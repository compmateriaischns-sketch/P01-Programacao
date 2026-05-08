vet = [int(input("Digite os elementos do vet: ")) for l in range(5)]

# Algoritmo de ordenação: Selection Sort
for i in range(len(vet)):
    # Encontra o índice do menor elemento no restante da lista
    k = i
    for j in range(i+1, len(vet)):
        if vet[j] < vet[k]:
            k = j
    # Troca o elemento atual com o menor encontrado
    vet[i], vet[k] = vet[k], vet[i]

print("Vetor ordenado em ordem crescente:", vet)
