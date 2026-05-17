v = int(input())
N = []
N.append(v)
a = v
for i in range(1,10,1):
    a = a*2
    N.append(a)
for i in range(10):
    print(f'N[{i}] = {N[i]}')