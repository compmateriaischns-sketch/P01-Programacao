nrpc1, qtdepc1, prpc1 = input().split()
nrpc2, qtdepc2, prpc2 = input().split()
nrpc1 = int(nrpc1)
qtdepc1 = int(qtdepc1)
prpc1 = float(prpc1)
nrpc2 = int(nrpc2)
qtdepc2 = int(qtdepc2)
prpc2 = float(prpc2)

vpc1 = qtdepc1*prpc1
vpc2 = qtdepc2*prpc2
total = vpc1+vpc2

print(f'VALOR A PAGAR: R$ {total:.2f}')