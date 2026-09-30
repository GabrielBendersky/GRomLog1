# 1. Define as dimensões desejadas
linhas = 3

colunas = 3

# 2. Cria a matriz 3x3 zerada de forma limpa
matriz = [[0] * colunas for i in range(linhas)]

# 3. Preenche e exibe usando len()
for i in range(len(matriz)):
    for j in range(len(matriz[0])):

        #salvando a minha linha e coluna na matriz 
        matriz[i][j] = (i * len(matriz[0])) + j

        #imprimindo o valor
        print(f"[{i}][{j}] = {matriz[i][j]}")


