#Multiplicação de Matriz por Escalar
#Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
#números inteiros e, em seguida, peça ao usuário um valor numérico constante
#(escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada
#elemento da matriz original por esse valor escalar e exibir a matriz resultante
#formatada em linhas e colunas.


def multiplicar_matriz():
    linhas = 3
    colunas = 3
    matriz1 = []


    # Leitura da matriz
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz1.append(linha)   



    # Leitura do valor escalar
    escalar = int(input("\nDigite o valor escalar: "))  

    # Multiplicação da matriz pelo escalar
    matriz_resultante = []
    for i in range(linhas):
        linha_resultante = []
        for j in range(colunas):
            linha_resultante.append(matriz1[i][j] * escalar)
        matriz_resultante.append(linha_resultante)




    # Impressão da matriz resultante
    print("\nMatriz resultante após a multiplicação pelo escalar:")       
    for linha in matriz_resultante:
        print(linha)


multiplicar_matriz()