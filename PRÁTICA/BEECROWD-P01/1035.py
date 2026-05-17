A, B, C, D = input().split(' ')

A = int(A)
B = int(B)
C = int(C)
D = int(D)
 
if B > C and D > A:
    if (C + D) > (A + B):
        if C > 0 and D > 0:
            if (A % 2) == 0:
                print('Valores aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')
     