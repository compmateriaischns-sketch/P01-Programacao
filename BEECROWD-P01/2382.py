L,A,P,R = input().split()
L=int(L)
A=int(A)
P=int(P)
R=int(R)

D = ((A*A)+(L*L)+(P*P))**(1/2)

if D <= 2*R:
    print('S')
else:
    print('N')