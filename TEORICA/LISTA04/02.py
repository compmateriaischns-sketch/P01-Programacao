vetor = [int(input("Digite os elementos do vetor: ")) for i in range(10)]

x = int(input("Digite x: "))

for i in range(10):
    if vetor[i] < x:
        print(vetor[i])

