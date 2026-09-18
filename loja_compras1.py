#programa de registro de vendas de uma loja ao longo do dia
# auto atendimento - cliente digita 1 para iniciar compra e 0 para finalizar
#para cada cliente, utilize o while para registrar o valor de cada valor comprado, e ao final do dia, exiba o total de vendas e a quantidade de clientes atendidos.
#descontos para valores a cima de R$200 aplica 10% de desconto, valores a cima de R$100 aplica 5% de desconto, valores abaixo de R$100 não aplicam desconto.
#cliente se deseja parcelar a compra e emita a possibilidade de 1  a 6 parcelas, com valor exato de cada parcela mensal 
# ao final do expediente o logista deve digitar 2 para finalizar o dia e exibir o total de vendas e a quantidade de clientes atendidos.
#não printar o resultado de vendas da loja para o cliente, apenas para o lojista. O cliente deve apenas receber o valor final da compra e a quantidade de parcelas caso tenha parcelado.

#total_compra = 0  
#aplicar_desconto = (200, 0.10), (100, 0.05)  # Tupla de descontos
#Parcelar = int(input("Deseja parcelar a compra? Digite 1 para sim ou 0 para não: "))
#quantidade_de_parcelas = int(input("Digite a quantidade de parcelas desejadas (1 a 6): "))
#quantidade_de_clientes_atendidos = 0






# INICIANDO A LOJA 
print("Bom dia! Bem-vindo ao auto atendimento ROMER'S STORE onde a Magia acontece.")

TOTAL_DE_VENDAS = 0.0
TOTAL_DE_CLIENTES_ATENDIDOS = 0
vendas_clientes = []  # Lista para salvar o valor pago por cliente 


# Inicio do Sistema de Atendimento
romer_story_diaria = int(input("\nDigite 1 para iniciar o atendimento ou 2 para fechar a loja: "))


#loop do cliente 

while romer_story_diaria != 2:
    if romer_story_diaria == 1:
        TOTAL_DE_CLIENTES_ATENDIDOS += 1
        print(f"\n--- Atendimento Cliente #{TOTAL_DE_CLIENTES_ATENDIDOS} ---")


        #Registrando o valor da compra
        valor_compra = float(input("Digite o valor da compra: R$ "))

        #aplicar desconto
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

        # Parcelamento
        parcelar = int(input("Deseja parcelar a compra? Digite 1 para sim ou 0 para não: "))
        if parcelar == 1:
            quantidade_de_parcelas = int(input("Digite a quantidade de parcelas desejadas (1 a 6): "))
            if 1 <= quantidade_de_parcelas <= 6:
                valor_parcela = valor_compra / quantidade_de_parcelas
                print(f"Compra parcelada em {quantidade_de_parcelas}x de R$ {valor_parcela:.2f}")
            else:
                print("Compra à vista.")


        # Registrando no caixa e na lista de vendas do dia
        TOTAL_DE_VENDAS += valor_compra
        vendas_clientes.append(valor_compra)

        print("\nObrigado por comprar Na ROMER'S STORE! Volte sempre e não compre na loja do YURI!")
        print("---------------------ROMER'S STORE---------------------------")

    # Solicita a próxima ação
    romer_story_diaria = int(input("\nDigite 1 para iniciar a compra ou 2 para fechar a loja:"))

#Area Exclusiva do Romer

print("\nÁrea exclusiva do Romer. Digite a senha para acessar o relatório de vendas.")
print("---------------------ROMER'S STORE---------------------------")
print("\n==================$$$$$$$$$$$$$$$$$$$$$$$$$$==============================")


senha = input("Digite a senha para ver o relatório do dia: ")
if senha == "123456":
    print("\n--- RESUMO DE VENDAS DO DIA ---")
    for indice, valor in enumerate(vendas_clientes, start=1):
        print(f"  • Cliente {indice}: R$ {valor:.2f}")
    
    print(f"\nTotal arrecadado pela loja: R$ {TOTAL_DE_VENDAS:.2f}")
    print("\nTenha um ótimo dia!")
else:
    print("\nSenha incorreta! Acesso ao relatório de vendas negado.")
    print("Obrigado por utilizar o auto atendimento ROMER'S STORE.")


