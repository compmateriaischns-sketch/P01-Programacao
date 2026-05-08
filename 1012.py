A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

area1 = A*C/2
area2 = 3.14159*(C**2)
area3 = (A+B)*C/2
area4 = B*B
area5 = A*B

print(f'TRIANGULO: {area1:.3f}')
print(f'CIRCULO: {area2:.3f}')
print(f'TRAPEZIO: {area3:.3f}')
print(f'QUADRADO: {area4:.3f}')
print(f'RETANGULO: {area5:.3f}')