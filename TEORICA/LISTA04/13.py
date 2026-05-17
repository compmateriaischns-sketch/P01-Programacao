q = int(input("Digite a quantidade de cargas descarregadas: "))
p, v = 0, 0
for i in range(1,q+1,1):
    p = float(input(f"Digite o peso da caixa {i}: "))
    p += p
    v = float(input(f'Digite o preço da caixa {i}: '))
    v += v

mon = float(input("Digite o valor monterário total: "))

print(f'Peso total das caixas: {p}', end='\n')
print(f'Valor total das caixas: {v}', end='\n')

if mon != v:
    print("O valor monetário total é diferente da soma dos preços das caixas.")