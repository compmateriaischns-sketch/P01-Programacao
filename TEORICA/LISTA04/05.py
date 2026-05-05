n = int(input("Informe o tamanho do vetor: "))
soma = 0
v = [int(input("Digite os elementos do vetor: ")) for i in range(n)]
for i in range(0,n,2):
    soma += v[i]

print(soma)


