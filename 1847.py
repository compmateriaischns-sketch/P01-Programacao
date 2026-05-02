A, B, C = input("Digite as temnperaturas: ").split()
A = int(A)
B = int(B)
C = int(C)
if (A > B) and (B <= C):
    print(':)')
elif (A < B) and (B >= C):
    print(':(')
elif (A < B) and (B < C) and (C-B) < (B-A):
    print(':(')
elif (A < B) and (B < C) and (C-B) >= (B-A):
     print(':)')
elif (A > B) and (B > C) and (B-C) < (A-B):
    print(':)')
elif (A > B) and (B > C) and (B-C) >= (A-B):
    print(':(')
else:
    if A == B and C > B:
        print(':)')
    else:
        print(':(')
