k = 0
while True:
    m = []
    c = []
    cm = []
    k += 1
    soma = 0
    sum = 0
    n = int(input("Digite a quantidade de imóveis: "))
    if n == 0:
        break
    for i in range(n):
        a, b = map(int,input("Morador Consumo: ").split())
        m.append(a)
        c.append(b)
        soma = soma + b
        sum = sum + a
        cm.append(b//a)
    maior = []
    outro = []
    j=0
    i=0
    for i in range(len(cm)):
        mm=0
        for j in range(j+i,len(cm)-i):
            if cm[j] < mm:
                mm = cm[j]
                outro.append(m[j])
        maior.append(mm)
    
    for i in range(1,k+1):
        print(f"Cidade# {i}:", end='\n')
        for j in range(n):
            print(f'{outro[j]}-{maior[j]}', end = " ")
        print(f"Consumo medio: {(soma/sum):.2f} m³.")