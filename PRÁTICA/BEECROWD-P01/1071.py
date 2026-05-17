x = int(input())
y = int(input())
soma = 0

if x > y:
    maior = x
    menor = y
if y >= x:
    maior = y
    menor = x


for i in range (menor + 1, maior):
    if i % 2 != 0:
        soma = soma + i

print (soma)