#Somatório de Números Ímpares em Intervalo Fechado
#Desenvolva um programa que solicite dois números inteiros representando os
#limites de um intervalo [A, B] (garantindo que A ≤ B). O programa deve iterar sobre
#o intervalo utilizando uma estrutura de repetição e calcular a soma apenas dos
#números ímpares presentes nele, exibindo o resultado final ao usuário.


def somatorio_impares():
    while True:
        A = int(input("Digite o valor de A (limite inferior): "))
        B = int(input("Digite o valor de B (limite superior): "))
        
        # Garantir que A seja menor ou igual a B
        if A <= B:
            break

        print("Erro: O valor de A deve ser menor ou igual a B. Tente novamente.\n")

    soma_impares = 0

    for numero in range(A, B + 1):
        if numero % 2 != 0:  # Verifica se o número é ímpar
            soma_impares += numero

    print(f"\nA soma dos números ímpares no intervalo [{A}, {B}] é: {soma_impares}")

somatorio_impares()




