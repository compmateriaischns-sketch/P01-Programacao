"""

Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).
Entrada

O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.
Saída

Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
Exemplo de Entrada 	Exemplo de Saída

5 2
6 3
5 0
	

2 3 4 5 Sum=14
3 4 5 6 Sum=18 
"""



while True:
    # Lê os dois valores na mesma linha
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])

    # Condição de parada: se qualquer um for menor ou igual a zero
    if m <= 0 or n <= 0:
        break

    # Identifica o menor e o maior para montar a sequência corretamente
    menor = min(m, n)
    maior = max(m, n)

    soma = 0
    sequencia_str = ""

    # Percorre do menor ao maior
    for i in range(menor, maior + 1):
        soma += i
        sequencia_str += str(i) + " "

    # Exibe a sequência seguida da soma total
    print(f"{sequencia_str}Sum={soma}")