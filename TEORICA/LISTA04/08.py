# v1 = []
# v2 = []
# v3 = []
v1, v2, v3 = [], [], []
for i in range(5):
    v = int(input("Digite um elemento do vetor 1: "))
    v1.append(v)
for i in range(5):
    v = int(input("Digite um elemento do vetor 2: "))
    v2.append(v)
for i in range(5):
    soma = v1[i] + v2[i]
    v3.append(soma)
print(*v3)