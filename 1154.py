soma = 0
n = 0
teste = True
while teste:
    idade = int(input("Digite a idade: "))
    if idade >= 0:
        soma = soma + idade
        n += 1
    else:
        teste = False
media = soma / n
print(f'{media:.2f}')        
