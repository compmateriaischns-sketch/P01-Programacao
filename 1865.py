n = int(input())

for i in range(n):
    nome,forca = input().split(' ')
    
    if nome.upper() == 'THOR':
       print('Y')
    else:
        print('N')