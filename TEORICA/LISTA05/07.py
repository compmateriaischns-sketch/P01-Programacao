
v = []
v = [int(input("Digite os elementos do vetor: ")) for i in range(50)]
a = len(v)//2
for j in range(a):
    k = len(v) - j - 1
    v[j], v[k] = v[k], v[j]
    # Outra opção:
    # b = v[j]
    # v[j] = v[k]
    # v[k] = b
print(v)