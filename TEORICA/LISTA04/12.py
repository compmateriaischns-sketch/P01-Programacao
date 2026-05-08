vid = []
vv = []
id = 1
soma = 0
k = 0
while id >= 0:
    id = input("Digite o ID: ")
    id = int(id)
    if id < 0:
        break
    v = input("Digite o valor: ")
    v = float(v)
    soma = soma + v
    vid.append(id)
    vv.append(v) 
    k += 1
print("Lista de dados do Lava-jato: ")
for i in range(k):
    print("ID:", vid[i], "- Valor:", vv[i])
print("Soma dos valores:", soma)