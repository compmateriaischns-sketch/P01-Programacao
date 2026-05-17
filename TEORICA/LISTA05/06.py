import random
v = [random.randint(1, 10) for i in range(100)]
n = int(input("Digite o valor de N: "))
k = 0
# print(v)
for j in range(100):
    if n == v[j]:
        print(f'O valor digitado está no vetor.')
        k += 1
if k == 0:
    print('O valor digitado não está no vetor.')