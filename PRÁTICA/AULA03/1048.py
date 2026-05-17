salario = float(input())
# salario_2 = round(salario, 2)

if salario >= 0 and salario <= 400.00:
    reajuste = salario * 0.15
    reajuste_2 = round(reajuste, 2)
    novo = salario + reajuste_2
    novo_2 = round(novo, 2) 
    print(f'Novo salario: {novo_2:.2f}')
    print(f'Reajuste ganho: {reajuste_2:.2f}')
    print('Em percentual: 15 %')
elif salario >= 400.01 and salario <= 800.00:
    reajuste = salario * 0.12
    reajuste_2 = round(reajuste, 2)
    novo = salario + reajuste_2
    novo_2 = round(novo, 2) 
    print(f'Novo salario: {novo_2:.2f}')
    print(f'Reajuste ganho: {reajuste_2:.2f}')
    print('Em percentual: 12 %')
elif salario >= 800.01 and salario <= 1200.00:
    reajuste = salario * 0.10
    reajuste_2 = round(reajuste, 2)
    novo = salario + reajuste_2
    novo_2 = round(novo, 2) 
    print(f'Novo salario: {novo_2:.2f}')
    print(f'Reajuste ganho: {reajuste_2:.2f}')
    print('Em percentual: 10 %')
elif salario >= 1200.01 and salario <= 2000.00:
    reajuste = salario * 0.07
    reajuste_2 = round(reajuste, 2)
    novo = salario + reajuste_2
    novo_2 = round(novo, 2) 
    print(f'Novo salario: {novo_2:.2f}')
    print(f'Reajuste ganho: {reajuste_2:.2f}')
    print('Em percentual: 7 %')
else: 
    reajuste = salario * 0.04
    reajuste_2 = round(reajuste, 2)
    novo = salario + reajuste_2
    novo_2 = round(novo, 2) 
    print(f'Novo salario: {novo_2:.2f}')
    print(f'Reajuste ganho: {reajuste_2:.2f}')
    print('Em percentual: 4 %')