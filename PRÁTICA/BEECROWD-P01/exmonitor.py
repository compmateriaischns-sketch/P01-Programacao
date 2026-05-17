n = int(input("Digite a quantidade de pés de sapato: "))

m39, d39, e39 = 0, 0, 0 
m40, d40, e40 = 0, 0, 0  
m41, d41, e41 = 0, 0, 0  
m42, d42, e42 = 0, 0, 0 
m43, d43, e43 = 0, 0, 0 
i = 0
if n % 2 != 0:
    print("Quantidade de botas deve ser par!")
else:
    while i < n:
        m, l = input("Tamanho Lado: ").split(' ')
        m = int(m)
        l = str(l)
        i += 1
        if m!= 39 and m!= 40 and m!= 41 and m!= 42 and m!= 43:
            i -= 1
            print("Tamanho inválido!")
            continue
           
        if m == 39:
            m39 += 1
            if l == 'D':
                d39 += 1
            elif l == 'E':
                e39 += 1
            else: 
                print('Lado inválido')
                i -= 1
        elif m == 40:
            m40 += 1
            if l == 'D':
                d40 += 1
            elif l == 'E':
                e40 += 1
            else: 
                print('Lado inválido') 
                i -= 1
        elif m == 41:
            m41 += 1
            if l == 'D':
                d41 += 1
            elif l == 'E':
                e41 += 1
            else: 
                print('Lado inválido')
                i -= 1
        elif m == 42:
            m42 += 1
            if l == 'D':
                d42 += 1
            elif l == 'E':
                e42 += 1
            else: 
                print('Lado inválido') 
                i -= 1
        elif m == 43:
            m43 += 1
            if l == 'D':
                d43 += 1
            elif l == 'E':
                e43 += 1
            else: 
                print('Lado inválido')
                i -= 1 
       
p = 0

while d39 > 0 and e39 > 0:
    d39 -= 1
    e39 -= 1
    p += 1
while d40 > 0 and e40 > 0:
    d40 -= 1
    e40 -= 1
    p += 1
while d41 > 0 and e41 > 0:
    d41 -= 1
    e41 -= 1
    p += 1
while d42 > 0 and e42 > 0:
    d42 -= 1
    e42 -= 1
    p += 1
while d43 > 0 and e43 > 0:
    d43 -= 1
    e43 -= 1
    p += 1

print(p)