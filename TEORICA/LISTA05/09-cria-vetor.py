# 1. Criação do arquivo .txt de exemplo (apenas para teste)
# O arquivo contém 30 números de 1 a 30, separados por espaço
with open('vetor.txt', 'w') as f:
    f.write(' '.join([str(i) for i in range(1, 31)]))

# 2. Algoritmo principal
def processar_vetor():
    try:
        # Lê o arquivo txt
        with open('vetor.txt', 'r') as file:
            conteudo = file.read()
            # Converte o conteúdo para uma lista de inteiros
            vetor = [int(x) for x in conteudo.split()]
        
        # Verifica se o vetor tem 30 posições
        if len(vetor) != 30:
            print(f"Alerta: O vetor tem {len(vetor)} posições, não 30.")

        # Altera as posições de índice par (0, 2, 4...) para 0
        for i in range(len(vetor)):
            if i % 2 == 0:
                vetor[i] = 0
        
        # Imprime o vetor atualizado
        print("Vetor atualizado (índices pares são 0):")
        print(vetor)
        
    except FileNotFoundError:
        print("Arquivo 'vetor.txt' não encontrado.")

# Executa a função
processar_vetor()
