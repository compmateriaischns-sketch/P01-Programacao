n = int(input())
tot, r, s, c = 0, 0, 0, 0
for i in range(1, n+1, 1):
    a, b = input().split(' ')
    a = int(a)
    b = str(b)
    tot = tot + a
    if b == 'R':
        r += a
    elif b == 'S':
        s += a
    elif b == 'C':
        c += a
print(f"Total: {tot} cobaias")
print("Total de coelhos:", c)
print("Total de ratos:", r)
print("Total de sapos:", s)
print(f"Percentual de coelhos: {c*100/tot:.2f} %")
print(f"Percentual de ratos: {r*100/tot:.2f} %")
print(f"Percentual de sapos: {s*100/tot:.2f} %")
