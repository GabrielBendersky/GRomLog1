#Exercício 3: Análise Térmica Semanal e Filtro de Desvio
#Implemente um programa que receba as temperaturas médias registradas durante
#os 7 dias da semana (armazenadas em um vetor de números reais). O programa
#deve calcular a média aritmética semanal e, em seguida, exibir quais temperaturas
#registradas ficaram estritamente abaixo dessa média.


def analise_temperaturas():
    temperaturas = []



    # Receber as temperaturas médias dos 7 dias da semana
    for i in range(7):
        temp = float(input(f"Digite a temperatura média do dia {i + 1}: "))
        temperaturas.append(temp)





    # Calcular a média aritmética semanal
    media_semanal = sum(temperaturas) / len(temperaturas)
    print(f"\nA média aritmética semanal das temperaturas é: {media_semanal:.2f}°C")






    # Exibir as temperaturas que ficaram estritamente abaixo da média
    print("\nTemperaturas abaixo da média:")
    for i, temp in enumerate(temperaturas):
        if temp < media_semanal:
            print(f"Dia {i + 1}: {temp:.2f}°C")


# Executar a função
analise_temperaturas()