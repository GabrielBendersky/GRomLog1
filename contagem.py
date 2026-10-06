def contagem_matriz_limiar():
    linhas = 2
    colunas = 4
    matriz = []

   
   
    # Leitura da matriz
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

   
   
    # Leitura do valor limite (limiar) 
    limiar = int(input("\nDigite o valor limite (limiar): "))

    
    
    # Contagem de elementos abaixo do limiar

    abaixo_limiar = 0
    for i in range(linhas): 
        for j in range(colunas):
            if matriz[i][j] < limiar:
                abaixo_limiar += 1


    
    # Impressão da matriz
    
    print("\nMatriz completa:")
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

    
    # Resultado da contagem
    print(f"\nTotal de valores abaixo do limiar ({limiar}): {abaixo_limiar}")



   
   
contagem_matriz_limiar()