import random

v = [random.randint(1,100) for i in range(1000)]
n = int(input("Digite um valor: "))
k = 0
for i in range(1000):
    if v[i] == n:
        k += 1
print(f'o número {n} aparece {k} vezes no vetor')
print(v)