
#programa de registro de vendas de uma loja ao longo do dia
# auto atendimento - cliente digita 1 para iniciar compra e 0 para finalizar
#para cada cliente, utilize o while para registrar o valor de cada valor comprado, e ao final do dia, exiba o total de vendas e a quantidade de clientes atendidos.
#descontos para valores a cima de R$200 aplica 10% de desconto, valores a cima de R$100 aplica 5% de desconto, valores abaixo de R$100 não aplicam desconto.
#cliente se deseja parcelar a compra e emita a possibilidade de 1  a 6 parcelas, com valor exato de cada parcela mensal 
# ao final do expediente o logista deve digitar 2 para finalizar o dia e exibir o total de vendas e a quantidade de clientes atendidos.


#total_compra = 0  
#aplicar_desconto = (200, 0.10), (100, 0.05)  # Tupla de descontos
#Parcelar = int(input("Deseja parcelar a compra? Digite 1 para sim ou 0 para não: "))
#quantidade_de_parcelas = int(input("Digite a quantidade de parcelas desejadas (1 a 6): "))
#quantidade_de_clientes_atendidos = 0


#INICIANDO A LOJA DE COMPRAS
print("Bom dia! Bem-vindo ao auto atendimento ROMER'S STOR&.")

TOTAL_DE_VENDAS = 0.0
TOTAL_DE_CLIENTES_ATENDIDOS = 0


#ENTRADA CLIENTE
Romer_story_diaria= int(input("Digite 1 para iniciar a compra ou 2 para finalizar o dia: "))

while Romer_story_diaria != 2:
    if Romer_story_diaria == 1:
        TOTAL_DE_CLIENTES_ATENDIDOS += 1    

        #REGISTRANDO VALOR DA COMPRA
        valor_compra = float(input("Digite o valor da compra: R$ "))

        #APLICANDO DESCONTOS
        if valor_compra > 200:
            desconto = valor_compra * 0.10
            valor_compra -= desconto
            print(f"Desconto de 10% aplicado! Valor final: R$ {valor_compra:.2f}")
        elif valor_compra > 100:
            desconto = valor_compra * 0.05
            valor_compra -= desconto
            print(f"Desconto de 5% aplicado! Valor final: R$ {valor_compra:.2f}")
        else:
            print(f"Sem desconto aplicado. Valor final: R$ {valor_compra:.2f}")

        #PARCELAMENTO
        Parcelar = int(input("Deseja parcelar a compra? Digite 1 para sim ou 0 para não: "))
        if Parcelar == 1:
        quantidade_de_parcelas = int(input("Digite a quantidade de parcelas desejadas (1 a 6): "))    
        if 1 <= quantidade_de_parcelas <= 6:
        valor_parcela = valor_compra / quantidade_de_parcelas
        print(f"Compra parcelada em {quantidade_de_parcelas}x de R$ {valor_parcela:.2f}")
            else:
        print("Quantidade de parcelas inválida. A compra será à vista.")
else:
            print("Compra à vista.")

    # REGISTRA NO CAIXA APÓS O DESCONTO
    TOTAL_DE_VENDAS += valor_compra

    print("\n------------------------------------------------")


 # SOLICITA A PRÓXIMA AÇÃO DENTRO DO LOOP
    Romer_story_diaria = int(
        input(
            "Digite 1 para o próximo cliente ou 2 para finalizar o dia e exibir"
            " o resumo: "
        )
    )

#FINALIZANDO O EXPEDIENTE


print(f"\nTotal de vendas do dia: R$ {TOTAL_DE_VENDAS:.2f}")
print(f"Quantidade de clientes atendidos: {TOTAL_DE_CLIENTES_ATENDIDOS}")
print("Obrigado por utilizar o auto atendimento ROMER'S STOR&. Tenha um ótimo dia!E NÃO COMPRE NA LOJA DO YURI")



