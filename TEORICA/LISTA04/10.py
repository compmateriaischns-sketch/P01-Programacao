# va, vn = [], []
# media = 5
# for i in range(5):
#     a, n = input("Altura Nome: ").split(" ")
#     a = float(a)
#     n = str(n)
#     if a > media:
#         va.append(a)
#         vn.append(n)

# print(vn)

va, vn = [], []
soma = 0
for i in range(10):
    a, n = input("Altura Nome: ").split(" ")
    a = float(a)
    n = str(n)
    va.append(a)
    vn.append(n)
    soma = soma + a

media = soma/10

for i in range(10):
    if va[i] > media:
        print(vn[i])


