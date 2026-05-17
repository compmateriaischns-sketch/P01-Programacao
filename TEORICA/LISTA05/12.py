# Nome dos arquivos
arquivo_valores = "valores.txt"
arquivo_produtos = "produtos.txt"

# 1. Ler os arquivos e criar vetores
with open(arquivo_valores, "r") as f:
    valores = [float(linha.strip()) for linha in f.readlines()]

with open(arquivo_produtos, "r") as f:
    produtos = [linha.strip() for linha in f.readlines()]

print("Vetor de valores:", valores)
print("Vetor de produtos:", produtos)

# 2. Encontrar maior e menor
maior = valores[0]
menor = valores[0]
k = 0  # índice do maior
m = 0  # índice do menor

for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
        k = i
    if valores[i] < menor:
        menor = valores[i]
        m = i

print(f'O produto mais caro é {produtos[k]} que custa R$ {valores[k]:.2f}')
print(f'O produto mais barato é {produtos[m]} que custa R$ {valores[m]:.2f}')

# 3. Buscar produto por nome
prod = input("Digite o nome de um produto: ")
for i in range(len(produtos)):
    if prod == produtos[i]:
        print(f'O produto {prod} custa R$ {valores[i]:.2f}')
        break
else:
    print(f'Produto {prod} não encontrado.')

