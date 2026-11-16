import csv
from pathlib import Path


def localizar_arquivo(caminho_arquivo: str | Path | None = None) -> Path:
    pasta_script = Path(__file__).resolve().parent
    caminhos = []

    if caminho_arquivo is not None:
        caminhos.append(Path(caminho_arquivo))

    caminhos.extend([
        pasta_script / "pedidos.csv",
        pasta_script.parent / "pedidos.csv",
        Path.cwd() / "pedidos.csv",

    ])

    for caminho in caminhos:
        if caminho.exists():
            return caminho

    return caminhos[0] if caminhos else pasta_script / "pedidos.csv"


def calcular_desconto(quantidade: int, valor_bruto: float) -> float:
    """Aplica a regra progressiva de desconto baseada na quantidade."""
    if quantidade >= 10:
        return valor_bruto * 0.10
    if 6 <= quantidade <= 9:
        return valor_bruto * 0.05
    if 3 <= quantidade <= 5:
        return valor_bruto * 0.03
    return 0.0


def formatar_linha(id_ped: str | int, cliente: str, bruto: str, desc: str, liquido: str, status: str) -> str:
    """Garante que o cabeçalho use a mesma largura de coluna."""
    return (
        f"{id_ped:<8} | {cliente:<22} | {bruto:>12} | {desc:>12} | {liquido:>13} | {status:<10}"
    )


def Auditoria_pedidos(caminho_arquivo: str | Path | None = None) -> None:
    arquivo = localizar_arquivo(caminho_arquivo)
    if not arquivo.exists():
        print(f"Erro: o caminho '{arquivo}' não existe.")
        return

    total_bruto = 0.0
    total_desconto = 0.0
    total_liquido = 0.0
    total_pedidos = 0
    maior_pedido = None
    menor_pedido = None

    with arquivo.open("r", encoding="utf-8", newline="") as arq:
        # 1. Corrigido delimiter para ";"
        leitor = csv.DictReader(arq, delimiter=";")

        if not leitor.fieldnames:
            print("Arquivo vazio")
            return

        cabecalho = formatar_linha("ID", "Cliente", "Valor Bruto", "Desconto", "Valor Liquido", "Status")
        largura_tabela = len(cabecalho)

        print("=" * largura_tabela)
        print(cabecalho)
        print("=" * largura_tabela)

        for num_linha, linha in enumerate(leitor, start=2):
            try:
                # 2. Corrigido ordem do .strip() antes do int()
                id_pedido = int(str(linha["id"]).strip())
                cliente = str(linha["cliente"]).strip()[:22]
                quantidade = int(str(linha["quantidade"]).strip())
                # 3. Corrigido nome da chave para "preco_unitario"
                valor_unitario = float(str(linha["preco_unitario"]).strip().replace(",", "."))
            except (KeyError, ValueError, AttributeError, TypeError) as erro:
                print(f"[AVISO] linha {num_linha} ignorada por dado inválido ({erro})")
                continue

            valor_bruto = quantidade * valor_unitario
            desconto = calcular_desconto(quantidade, valor_bruto)
            valor_liquido = valor_bruto - desconto
            status = "Aprovado" if valor_liquido > 1000 else "Reprovado"

            total_bruto += valor_bruto
            total_desconto += desconto
            total_liquido += valor_liquido
            total_pedidos += 1

            pedido_atual = {
                "id": id_pedido,
                "cliente": cliente,
                "valor_liquido": valor_liquido,
            }

            if maior_pedido is None or valor_liquido > maior_pedido["valor_liquido"]:
                maior_pedido = pedido_atual

            if menor_pedido is None or valor_liquido < menor_pedido["valor_liquido"]:
                menor_pedido = pedido_atual

            print(
                formatar_linha(
                    id_pedido,
                    cliente,
                    f"{valor_bruto:.2f}",
                    f"{desconto:.2f}",
                    f"{valor_liquido:.2f}",
                    status,
                )
            )

    if total_pedidos == 0:
        print("Nenhum pedido válido encontrado.")
        return

    print("=" * largura_tabela)
    print("Relatório final")
    print("=" * 45)
    print(f"Faturamento Bruto Total:      R$ {total_bruto:,.2f}")
    print(f"Total de Desconto Concedido:  R$ {total_desconto:,.2f}")
    print(f"Faturamento Líquido Total:    R$ {total_liquido:,.2f}")
    print(f"Pedidos Processados:          {total_pedidos}")
    # 4. Removidos os hífens e a quebra de linha no meio da string
    print(f"Maior Pedido:                 #{maior_pedido['id']} {maior_pedido['cliente']} (R$ {maior_pedido['valor_liquido']:,.2f})")
    print(f"Menor Pedido:                 #{menor_pedido['id']} {menor_pedido['cliente']} (R$ {menor_pedido['valor_liquido']:,.2f})")


if __name__ == "__main__":
    Auditoria_pedidos()