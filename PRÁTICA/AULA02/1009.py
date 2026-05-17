vendedor = str(input())
salario = float(input())
vendas = float(input())

comissao = vendas*0.15

receber = salario + comissao

print(f'TOTAL = R$ {receber:.2f}')
