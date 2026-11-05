#O almoxarifado de uma assistência técnica controla suas peças por meio de um arquivo chamado estoque_geral.csv
#(contendo colunas id, produto,saldo_atual e estoque_minimo).
#Desenvolva um script que leia esse arquivo e filtre apenas os itens cujo saldo_atual esteja estritamente abaixo do estoque_minimo.
#O resultado filtrado deve ser gravado em um novo arquivo chamado pedidos_reposicao.csv, incluindo uma nova coluna calculada chamada
#qtd_comprar, que representa a quantidade necessária para atingir a meta mínima.

import csv 


#abrir o arquivo de entrada e criar saida

with open("estoque_geral.csv", "r", encoding="utf-8") as arquivo_entrada, \
     open("pedidos_reposicao.csv", "w", newline="", encoding="utf-8") as arquivo_saida:

    leitor_csv = csv.DictReader(arquivo_entrada)

    #add coluna qtd_comprar e escrever cabecalho
    campos_saida = leitor_csv.fieldnames + ["qtd_comprar"]
    escritor_csv = csv.DictWriter(arquivo_saida, fieldnames=campos_saida)
    
    escritor_csv.writeheader()


    #filtrar e calcular 

    for linha in leitor_csv:
        saldo_atual = int(linha["saldo_atual"])
        estoque_minimo = int(linha["estoque_minimo"])

        if saldo_atual < estoque_minimo:
            linha["qtd_comprar"] = estoque_minimo - saldo_atual
            
            escritor_csv.writerow(linha)

print("Arquivo pedidos_reposicao.csv gerado com sucesso.")