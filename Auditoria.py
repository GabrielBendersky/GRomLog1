#Leitura do arq. conta cpessoal.csv

def auditoria_pedidos(nomearq="pedidos.csv"):
    total_bruto = 0.0
    total_liquido = 0.0
    total_desconto = 0.0
    total_pedidos = 0

    maiorPedido = None
    menorPedido = None

    try:
        with open(nomearq, "r", encoding="utf-8") as arq:
            cabeçalho = next(arq, None)
            if cabeçalho is None:
                print("Arquivo vazio")
                    

            print("=" * 80)
            print(f"{'ID':<10}{'Cliente':<30}{'Valor Bruto':<15}{'Desconto':<15}{'Valor Liquido':<15}")
            print("=" * 80)

            for linha in arq:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue

                campos = linha_limpa.split(";")
                if len(campos) < 5:
                    continue

                id_pedido = campos[0]
                cliente = campos[1]
                produto = campos[2]
                quantidade = int(campos[3])
                valor_unitario = float(campos[4])

                valor_bruto = quantidade * valor_unitario

                if quantidade >= 10:
                    desconto = valor_bruto * 0.10
                elif 6 <= quantidade <= 9:
                    desconto = valor_bruto * 0.05
                elif 3 <= quantidade <= 5:
                    desconto = valor_bruto * 0.03
                else:
                    desconto = 0.0

                valor_liquido = valor_bruto - desconto
                status = "Aprovado" if valor_liquido > 1000 else "Reprovado"

                total_bruto += valor_bruto
                total_desconto += desconto
                total_liquido += valor_liquido
                total_pedidos += 1

                if maiorPedido is None or valor_liquido > maiorPedido["valor_liquido"]:
                    maiorPedido = {"id": id_pedido, "cliente": cliente, "valor_liquido": valor_liquido}

                if menorPedido is None or valor_liquido < menorPedido["valor_liquido"]:
                    menorPedido = {"id": id_pedido, "cliente": cliente, "valor_liquido": valor_liquido}

                print(f"{id_pedido:<6}{cliente:<20}{valor_bruto:<12.2f}{desconto:<13.2f}{valor_liquido:<12.2f}{status:<8}")

            if total_pedidos == 0:
                print("Nenhum pedido encontrado.")
                return

            print("=" * 80)
            print("\nRelatório Final")
            print("=" * 45)
            print(f"Faturamento Bruto Total: {total_bruto:.2f}")
            print(f"Total de Desconto Concedido: {total_desconto:.2f}")
            print(f"Faturamento Líquido Total: {total_liquido:.2f}")
            print(f"Quantidade de Pedidos Processados: {total_pedidos}")
            print(f"Maior Pedido: {maiorPedido['id']} - {maiorPedido['cliente']} - {maiorPedido['valor_liquido']:.2f}")
            print(f"Menor Pedido: {menorPedido['id']} - {menorPedido['cliente']} - {menorPedido['valor_liquido']:.2f}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nomearq}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    auditoria_pedidos()
