"""Escreva um algoritmo que receba 100 valores de entrada de dados de informações de 
conta bancária de clientes. Para cada cliente será informado o número da conta, a agência 
e o saldo deste usuário. O algoritmo deve, após a leitura de todas as contas, escrever na 
tela cada uma das contas, os respectivos saldos e uma das mensagens: positivo/negativo. 
Ao final, também deverá escrever o total de clientes em cada agência, e o percentual de 
pessoas com saldo negativo daquela agência. """

clientes = []
agencias = []
saldos = []
tot_agencia = []
sneg = []

for i in range(4):
    conta = input("Digite o número da conta: ")
    agencia = input("Digite a agência: ")
    saldo = float(input("Digite o saldo: "))
    clientes.append(conta)
    agencias.append(agencia)
    saldos.append(saldo)

    
    
for n in range(4):
    tot_a, sn = 0, 0
    for m in range(4):
        if agencias[n] == agencias[m]:
            tot_a += 1
            if saldos[m] <= 0:
                sn += 1           
    tot_agencia.append(tot_a)
    sneg.append(sn)

for j in range(4):
    if saldos[j] >= 0:
        pn = 'Positivo'
    else:
        pn = 'Negativo'
    print(f'Conta: {clientes[j]} | Saldo: {saldos[j]:.2f} | Situação: {pn}')
    

for l in range(4):
    c = 0
    if l == 0:
        print(f'Agência: {agencias[l]} | Tot Clientes: {tot_agencia[l]} | Negativos: {(sneg[l]/tot_agencia[l])*100:.2f} %')
        continue
    for p in range(l):
        if agencias[l] == agencias[p]:
            c += 1

    if c == 0:       
        print(f'Agência: {agencias[l]} | Tot Clientes: {tot_agencia[l]} | Negativos: {(sneg[l]/tot_agencia[l])*100:.2f} %')
        
