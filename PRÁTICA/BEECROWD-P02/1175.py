N = [int(input()) for i in range(7)]
b = len(N)
print(N)
for i in range(b//2):
    a = N[i]
    N[i] = N[b-i-1]
    N[b-i-1] = a
for i in range(b):
    print(f'N[{i}] = {N[i]}')