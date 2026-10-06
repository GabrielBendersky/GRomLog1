#Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
#em seguida, solicite um número adicional para consulta. O sistema deve verificar e
#exibir se esse valor está presente no vetor e a quantidade exata de vezes que ele se
#repete.

def verificar_ocorrencias():
    lista = []





    # Ler 10 números inteiros e armazená-los em uma lista
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        lista.append(numero)




    # Solicitar um número adicional para consulta
    numero_consulta = int(input("Digite o número a ser consultado: "))

    
    
    # Verificar se o valor está presente no vetor e contar as ocorrências
    ocorrencias = lista.count(numero_consulta)
    if ocorrencias > 0:
        print(f"O número {numero_consulta} está presente na lista e se repete {ocorrencias} vez(es).")
    else:
        print(f"O número {numero_consulta} não está presente na lista.")

# Executar a função
verificar_ocorrencias()