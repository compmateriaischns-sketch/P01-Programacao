i = 0
vetor = []
while i < 5:
    i += 1
    v = int(input("Digite os elementos do vetor: "))
    if v >= 0 and v <= 10:
        vetor.append(v)
    else:
        i -= 1
print(vetor)