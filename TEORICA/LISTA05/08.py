import random
v1 = [random.randint(1, 100) for i in range(75)]
v2 = [random.randint(1, 100) for i in range(75)]
v3 = []
for i in range(75):
    a = v1[i] + v2[i]
    v3.append(a)
print(v1)
print(v2)
print(v3)