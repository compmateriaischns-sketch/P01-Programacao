a = 1
b = 1
Fib = []
for i in range(61):
    if i == 0:
        Fib.append(0)
        continue
    if i == 1 or i == 2:
        Fib.append(1)
        continue
    a, b = b, a+b
    Fib.append(b)
    
# print(Fib)

T = int(input("Interações"))
for i in range(T):
    n = int(input("N-ésimo termo de Fib"))
    print(f'Fib({n}) = {Fib[n]}')