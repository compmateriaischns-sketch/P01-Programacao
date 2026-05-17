x = int(input("Digite a quantidade de itens comprados: "))
nome, precod, precor, qtd, totr, totd = [], [], [], [], [], []
somar, somad = 0, 0
for i in range(x):
    produto = input('Digite o nome do produto: ')
    pd = float(input('Digite o preço do produto: '))
    q = int(input('Digite a quantidade de itens: '))
    nome.append(produto)
    precod.append(pd)
    pr = pd * 5.65
    qtd.append(q)
    precor.append(pr)
    td = pd * q
    tr = pr * q
    totd.append(td)
    totr.append(tr)

    somar += tr
    somad += td

for j in range(x):
    print(f'Nome: {nome[j]} | Total dólar: {totd[j]:.2f} | Total real: {totr[j]:.2f}')

print(f'Soma em real: {somar:.2f} | Soma em dolar: {somad:.2f}')


