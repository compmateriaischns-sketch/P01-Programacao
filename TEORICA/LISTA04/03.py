
vetor = [1, 2, 3, 4, 5]
n = float(input("Digite N: "))
teste = False
for i in range(5):
    if n == vetor[i]:
        print("N está na posição",i)
        teste = True

if teste == False:
    print("N não foi encontrado")