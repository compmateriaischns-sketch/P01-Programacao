A,G,Ra,Rg = input().split()

# A = f'{float(A):.2f}'
# G = f'{float(G):.2f}'
# Ra = f'{float(Ra):.2f}'
# Rg = f'{float(Rg):.2f}'

A = float(A)
A = round(A,2)
G = float(G)
G = round(G,2)
Ra = float(Ra)
Ra = round(Ra,2)
Rg = float(Rg)
Rg = round(Rg,2)

# print(A,G,Ra,Rg)

Ea = Ra/A
Eg = Rg/G

if Ea > Eg:
    print('A')
elif Eg > Ea:
    print('G')
else:
    print('G')