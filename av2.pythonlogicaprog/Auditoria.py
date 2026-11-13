# Auditoria de Pedidos
#A divisão de vendas precisa automatizar a apuração de pedidos comerciais.
#Programa que realize a leitura do arquivo estruturado pedidos.csv
#a) Tratamento de Arquivo:
#Abrir o arquivo utilizando tratamento de erros (try / except FileNotFoundError), exibindo mensagem amigável caso não seja localizado.
#b) Valor Bruto: Para cada pedido, calcular Valor Bruto = quantidade * preco_unitario.
#c) Desconto Progressivo: Se quantidade >= 10, aplicar 10% de desconto sobre o bruto; 
#se entre 6 e 9 (inclusive), aplicar 5% de desconto; se menos de 6, desconto de 0.00.
#d) Valor Líquido e Status: Calcular Valor Líquido = Valor Bruto - Desconto. Se valor líquido >= 1000.00, classificar como 'PREMIUM', senão 'PADRÃO'.
#e) Relatório Consolidado: 
#Exibir listagem tabular dos pedidos (ID, Cliente, Bruto, Desconto e Líquido em 2 casas decimais) e,
# ao final, Faturamento Bruto Total, Total de Descontos, Faturamento Líquido Total e dados do maior pedido líquido.






#leitura do arquivo estruturado pedidos.csv
def auditar_pedidos(nome_arquivos="pedidos.csv"):
    #variaveis
    total_bruto =0.0
    total_descontos = 0.0
    total_liquido = 0.0

    #rastrear pedidos de maior valor liquido
    maior_pedido = None

    #a) Tratamento de Arquivo: Abrir o arquivo utilizando tratamento de erros (try / except FileNotFoundError),
    # exibindo mensagem amigável caso não seja localizado.
    try:
        with open (nome_arquivos, mode="r", encoding="utf-8") as arquivo:
            #ignora cabeçalho
            cabeçalho = next(arquivo, None)
            if cabeçalho is None:
                print("Aviso: O arquivo CSV está vazio")
                return


            # e) Relatório Consolidado (Cabeçalho da tabela):
            # Exibir listagem tabular dos pedidos (ID, Cliente, Bruto, Desconto e Líquido em 2 casas decimais)

            print("=" * 88)
            print(
                f"{'ID':<6} | {'Cliente':<20} | {'Bruto (R$)':>12} | "
                f"{'Desconto (R$)':>13} | {'Líquido (R$)':>12} | {'Status':<8}"
            )
            print("-" * 88)



            #varredura de linha
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue   #pula linha em branco

                campos = linha_limpa.split(";")
                id_pedido = campos[0]
                cliente = campos[1]
                produto = campos[2]
                quantidade = int(campos[3])
                preco_unitario = float(campos[4])


                # b) Valor Bruto: Para cada pedido, calcular Valor Bruto = quantidade * preco_unitario.
                valor_bruto = quantidade * preco_unitario

                # c) Desconto Progressivo: Se quantidade >= 10, aplicar 10% de desconto sobre o bruto;
                # se entre 6 e 9 (inclusive), aplicar 5% de desconto; se menos de 6, desconto de 0.00.
                if quantidade >= 10:
                    desconto = valor_bruto * 0.10
                elif 6 <= quantidade <= 9:
                    desconto = valor_bruto * 0.05
                else:
                    desconto = 0.0

                # d) Valor Líquido e Status: Calcular Valor Líquido = Valor Bruto - Desconto.
                # Se valor líquido >= 1000.00, classificar como 'PREMIUM', senão 'PADRÃO'.

                valor_liquido = valor_bruto - desconto
                status = "PREMIUM" if valor_liquido > 1000 else "PADRÃO"

                #  Atualização das variáveis de controle  
                total_bruto += valor_bruto
                total_descontos += desconto
                total_liquido += valor_liquido

                #  Rastrear o pedido de maior valor líquido
                if maior_pedido is None or valor_liquido > maior_pedido["liquido"]:
                    maior_pedido = {"id": id_pedido, "cliente": cliente, "produto": produto,  "liquido": valor_liquido, "status": status}

                # e) Relatório Consolidado (Linhas da tabela):
                # Exibir listagem tabular dos pedidos (ID, Cliente, Bruto, Desconto e Líquido em 2 casas decimais)
                print(
                    f"{id_pedido:<6} | {cliente:<20} | {valor_bruto:>12.2f} | "
                    f"{desconto:>13.2f} | {valor_liquido:>12.2f} | {status:<8}"
                )
            # e) Relatório Consolidado (Fechamento):
            # Exibir ao final, Faturamento Bruto Total, Total de Descontos, Faturamento Líquido Total e dados do maior pedido líquido.
            print("=" * 88)
            print("=" * 88)
            print("\nRelatório consolidado:")
            print("-" * 45)
            print(f"Faturamento Bruto Total: R$ {total_bruto:.2f}")
            print(f"Total de Descontos: R$ {total_descontos:.2f}")
            print(f"Faturamento Líquido Total: R$ {total_liquido:.2f}")

            if maior_pedido:
                print("Pedido de Maior Valor Líquido:")
                print("-" * 45)
                print(
                    f"Pedido ID: {maior_pedido['id']}, Cliente: {maior_pedido['cliente']}, "
                    f"Produto: {maior_pedido['produto']}, Valor Líquido: R$ {maior_pedido['liquido']:.2f}, Status: {maior_pedido['status']}"
                )
    except FileNotFoundError:
            # a) Tratamento de Arquivo: exibindo mensagem amigável caso não seja localizado.
            print(f"Erro: O arquivo '{nome_arquivos}' não foi encontrado."
                    "Verifique se o nome do arquivo está correto e tente novamente."          
            )
if __name__ == "__main__":
    auditar_pedidos()        
                