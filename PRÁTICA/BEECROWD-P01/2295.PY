A,G,Ra,Rg = input().split()

A = float(A)
A = round(A,2)
G = float(G)
G = round(G,2)
Ra = float(Ra)
Ra = round(Ra,2)
Rg = float(Rg)
Rg = round(Rg,2)

Ea = Ra/A
Eg = Rg/G

if Ea > Eg:
    print('A')
elif Eg > Ea:
    print('G')
else:
    print('G')