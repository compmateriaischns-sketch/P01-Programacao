"""

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
Entrada

O arquivo de entrada contém um valor inteiro N.
Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
Exemplo de Entrada 	Exemplo de Saída

556
	

0:9:16

1
	

0:0:1

140153
	

38:55:53"""

n = int(input())
horas = 0
minutos = 0
segundos = 0
if n >= 3600:
    while n >= 3600:
        horas += 1
        n -= 3600
if n >= 60 and n < 3600:
    while n >= 60:
        minutos += 1
        n -= 60
if n < 60:
    segundos = n

print(f'{horas}:{minutos}:{segundos}')