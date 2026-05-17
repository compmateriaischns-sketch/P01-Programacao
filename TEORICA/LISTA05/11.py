import random
t = [random.randint(15, 40) for i in range(121)]
soma = 0
for i in range(121):
    soma += t[i]
media = soma/121
print(f'A temperatura média é {media:.1f}')
k, a, b = 0, 0, 0
for i in range(121):
    if t[i] < media:
        k += 1
    if t[i] < 20:
        a += 1
    if t[i] > 35:
        b += 1
print(f'Em {k} dias a temperatura foi inferior à média.')
print(f'Em {a} dias a temperatura foi inferior a 20ºC.')
print(f'Em {b} dias a temperatura foi superior a 35ºC')
