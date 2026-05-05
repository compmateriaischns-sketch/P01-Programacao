vet = [float(input("Digite os elementos do vet: ")) for l in range(5)]
menor = 999999999
menor = float(menor)
vcrescente = []
for j in range(5):
    for i in range(5):
        vet[i] = float(vet[i])
        if vet[i] < menor:
            menor = vet[i]
            k = i
    vcrescente.append(menor)
    vet[k] = ''

print(vcrescente)
