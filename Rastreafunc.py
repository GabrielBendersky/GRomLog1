from datetime import datetime


def registrar_evento(usuario: str, acao: str, status: str) -> None:
    # Captura a data e a hora exatas no momento da execução
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Formata a linha de registro padronizada
    registro = (
        f"[{data_hora}] USUARIO: {usuario} | ACAO: {acao.upper()} | STATUS:"
        f" {status.upper()}\n"
    )

    # Abre o arquivo em modo 'a' (append) para adicionar ao final sem sobrescrever
    with open("auditoria_sistema.log", mode="a", encoding="utf-8") as arquivo:
        arquivo.write(registro)


# Exemplos de uso:
registrar_evento("ana.silva", "LOGIN", "SUCESSO")
registrar_evento("carlos.mendes", "SAQUE", "FALHA")
registrar_evento("admin", "EXCLUSAO", "SUCESSO")