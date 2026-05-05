salario = float(input())
salario = round(salario, 2)

if salario <= 2000:
    print('Isento')
else:
    imp = 0
    if salario <= 3000:
        imp = (salario - 2000)*0.08
    elif salario <= 4500:
        imp = (1000*0.08) + (salario - 3000)*0.18
    else:
        imp = 1000*0.08 + 1500*0.18 + (salario - 4500)*0.28
    
    print(f'R$ {imp:.2f}')