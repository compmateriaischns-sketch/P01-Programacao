vetor = []
soma = 0
for i in range(5):
    v = float(input("Digite a nota: "))
    vetor.append(v)
    soma = soma + v
    
media = soma/15
print(media)