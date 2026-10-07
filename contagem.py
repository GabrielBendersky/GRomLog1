#Exercício 5: Contagem de Valores Menores que um Limiar em Matriz
#Retangular
#Desenvolva um programa que leia os valores de uma matriz 2 × 4 de números
#inteiros. O programa deve contar quantos valores estão abaixo de um limiar, que
#também será informado pelo usuário, estão presentes na estrutura e exibir a
#contagem total, além de imprimir a matriz completa formatada em linhas e colunas.


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