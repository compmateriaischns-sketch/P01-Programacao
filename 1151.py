N = int(input())

a = 0
b = 1
i = 2
v = [a, b]
while i < N:
    a, b = b, a + b
    v.append(b)
    i += 1
    
    
print(*v)