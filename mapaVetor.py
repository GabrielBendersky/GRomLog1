#Exercício 4: Mapeamento Condicional de Vetor
#Construa um programa que receba 8 números inteiros e os guarde em um vetor. Em
#seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares do
#vetor original sejam multiplicados por 2 e os números pares permaneçam
#inalterados. Ao final, exiba os dois vetores.




def mapeamento_condicional():   
    vetor_original = []
    vetor_mapeado = []

    # Receber 8 números inteiros e armazená-los no vetor original
    for i in range(8):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor_original.append(numero)

    # Mapear os números conforme a condição
    for numero in vetor_original:
        if numero % 2 != 0:  # Verifica se o número é ímpar
            vetor_mapeado.append(numero * 2)
        else:
            vetor_mapeado.append(numero)

    # Exibir os dois vetores
    print("\nVetor original:")
    print(vetor_original)
    print("\nVetor mapeado:")
    print(vetor_mapeado)


    
mapeamento_condicional()