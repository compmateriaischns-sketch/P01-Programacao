v = [int(input("Digite os elementos do vertor: ")) for i in range(10)]
for i in range(10):
    if v[i] <= 0:
        v[i] = 1
    print(f"X[{i}] = {v[i]}")