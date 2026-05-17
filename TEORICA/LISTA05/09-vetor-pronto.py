# Nome do arquivo
arquivo_nome = "vetor1.txt"

try:
    # 1. Ler o arquivo txt
    with open(arquivo_nome, "r") as arquivo:
        # Lê todas as linhas, remove quebras de linha e converte para inteiro
        # Assume que o arquivo tem 30 números válidos
        vetor = [int(linha.strip()) for linha in arquivo if linha.strip()]

    if len(vetor) != 30:
        print(f"Atenção: O arquivo contém {len(vetor)} elementos, não 5.")

    print("Vetor original:", vetor)

    # 2. Alterar posições de índice par (0, 2, 4...) para 0
    # Em Python, índices começam em 0 (par, ímpar, par, ímpar...)
    for i in range(len(vetor)):
        if i % 2 == 0:  # Verifica se o índice é par
            vetor[i] = 0

    # 3. Imprimir o vetor atualizado
    print("Vetor atualizado (índices pares são 0):")
    print(vetor)

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_nome}' não foi encontrado.")
except ValueError:
    print("Erro: O arquivo contém dados que não podem ser convertidos para números.")
