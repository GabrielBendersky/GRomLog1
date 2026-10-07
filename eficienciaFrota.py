def Monitoramento_frota():
    # Implementação da função de monitoramento
    total_veiculos = 0
    total_km = 0.0
    total_litros = 0.0

    # INICIANDO O SISTEMA ROMER DE MONITORAMENTO DE FROTA 
    print ("Bem-vindo ao sistema ROMER de monitoramento de frota!")
    print ("digite 0 para finalizar o expediente e exibir o total de veículos, km rodados e litros abastecidos.")

    # Loop para monitoramento de veículos
    while True:
        distancia = float(input("Digite a distância percorrida pelo veículo (em km): "))
        if distancia <= 0:
            break
        
        # Solicitando a quantidade de litros abastecidos 
        litros = float(input("Digite a quantidade de litros abastecidos: "))
        while litros <= 0:
            print("Quantidade de litros inválida. Por favor, digite um valor positivo.")

            # pede os litros novamente. 
            litros = float(input("Digite a quantidade de litros abastecidos: "))

        # Cálculo do consumo médio 
        consumo_medio = distancia / litros

        # classificação do consumo médio do veiculo
        
        if consumo_medio >= 12.0:
            classificacao = "Econômico"
        elif consumo_medio >= 9.0 and consumo_medio < 12.0:
            classificacao = "Padrão"
        else:
            classificacao = "Alto consumo"
        print(f"Consumo médio do veículo: {consumo_medio:.2f} km/l - Classificação: {classificacao}")

        # Desempenho da frota 

        # Acumuladores
        total_veiculos += 1
        total_km += distancia
        total_litros += litros

    # exibir relatorio final 
    print("\n---------------------- Relatório Final----------------------")
    print(f"Total de veículos: {total_veiculos}")
    print(f"Total de km rodados: {total_km:.1f} km")
    print(f"Total de litros: {total_litros:.1f} L")

    if total_veiculos > 0 and total_litros > 0:
        consumo_medio_frota = total_km / total_litros
        print(f"\tConsumo médio da frota: {consumo_medio_frota:.2f} km/l")
    else:
        print("\tConsumo médio da frota: Não houve veiculos auditados.")


# executando a função de monitoramento da frota
Monitoramento_frota()





#pra editar o texto de uma vez ctrl +h  