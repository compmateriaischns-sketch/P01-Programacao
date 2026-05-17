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

# # Lista com os valores das notas disponíveis
# imposto = [2000, 1000, 1500]
# imp = 0

# # Itera sobre cada nota para calcular a quantidade necessária
# for tx in imposto:
#     if tx == 2000:
#         salario = salario - 2000
#         if salario <= 0:
#             print('Isento')
#             break
#     elif tx == 1000:
#         salario = salario - 1000
#         if salario <= 0:
#             break
#         imp = imp + 1000*0.08            
#     elif tx == 1500:
#         salario = salario - 1500
#         if salario <= 0:
#             break
#         imp = imp + imposto*0.18     
        
#     else:
#         imp = imp + salario*0.28
    
#     print(imp)




# if salario >= 2000:
#     imp = salario - 2000
# elif salario > 2000:
#     p1 = salario - 2000
