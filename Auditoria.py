# Leitura do arq. conta pedidos.csv
from pathlib import Path


def localizar_arquivo(nomearq="pedidos.csv") -> Path:
    pasta_script = Path(__file__).resolve().parent
    caminhos = [
        Path(nomearq),
        pasta_script / nomearq,
        pasta_script.parent / nomearq,
        Path.cwd() / nomearq,
        Path.cwd() / "Em casa" / nomearq,
    ]

    for caminho in caminhos:
        if caminho.exists():
            return caminho

    return caminhos[0]


def auditoria_pedidos(nomearq="pedidos.csv"):
    total_bruto = 0.0
    total_liquido = 0.0
    total_desconto = 0.0
    total_pedidos = 0

    maiorPedido = None
    menorPedido = None
    arquivo = localizar_arquivo(nomearq)

    try:
        with open(arquivo, "r", encoding="utf-8") as arq:
            cabecalho = next(arq, None)
            if cabecalho is None:
                print("Arquivo vazio")
                return

            print("=" * 80)
            print(f"{'ID':<6}{'Cliente':<22}{'Valor Bruto':<14}{'Desconto':<12}{'Valor Liquido':<16}{'Status':<10}")
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
                valor_unitario = float(campos[4].replace(",", "."))

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

                print(f"{id_pedido:<6}{cliente:<22}{valor_bruto:<14.2f}{desconto:<12.2f}{valor_liquido:<16.2f}{status:<10}")

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
            print(f"Maior Pedido: {maiorPedido['id']} - {maiorPedido['cliente']} - R$ {maiorPedido['valor_liquido']:.2f}")
            print(f"Menor Pedido: {menorPedido['id']} - {menorPedido['cliente']} - R$ {menorPedido['valor_liquido']:.2f}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    auditoria_pedidos()