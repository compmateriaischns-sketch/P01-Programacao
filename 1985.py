p = int(input("Qtd de produtos comprados: "))
i = 0
v = []
problema = ''
soma = 0
tot = 0
while i < p:
    prod, q = map(int, input("Digite o codigo do produto espaco a quantidade ").split(" "))
    v.append(prod)
    for j in range(i):
        if prod == v[j]:
            print("Esse produto ja foi informado. Corrija.")
            problema = 'erro'                
            break
    if problema != 'erro':
        soma = q + soma
        i += 1
    else:
        problema = ''
        continue  
    if prod == 1001:
        tot = tot + q*1.50
    elif prod == 1002:
        tot = tot + q*2.50
    elif prod == 1003:
        tot = tot + q*3.50
    elif prod == 1004:
        tot = tot + q*4.50
    elif prod == 1005:
        tot = tot + q*5.50

print(f'{tot:.2f}') 