#O setor de segurança da informação de uma empresa precisa rastrear as ações dos funcionários no sistema corporativo.
#i. Crie uma função em Python chamada registrar_evento(usuario, acao, status) que receba o nome do usuário, a ação executada (ex: LOGIN, SAQUE, EXCLUSAO)
#e o status da operação (SUCESSO ou FALHA).
# O programa deve anexar cada registro em uma nova linha no arquivo
#auditoria_sistema.log, contendo a data e a hora do momento exato em que a ação
#ocorreu, sem sobrescrever os registros anteriores.



from datetime import datetime

def registrar_evento(usuario: str, acao: str, status: str) -> None:
    # Obter a data e hora atual
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formatar a linha de registro (em uma única linha)
    registro = f"[{data_hora_atual}] Usuário: {usuario}, Ação: {acao}, Status: {status}\n"
    
    # Anexar o registro garantindo o suporte a acentos (utf-8)
    with open("auditoria_sistema.log", "a", encoding="utf-8") as arquivo_log:
        arquivo_log.write(registro)

if __name__ == "__main__":
    # Exemplo de uso da função registrar_evento
    registrar_evento("joao.silva", "LOGIN", "SUCESSO")
    registrar_evento("maria.souza", "EXCLUSAO", "FALHA")
    registrar_evento("carlos.lima", "SAQUE", "SUCESSO")
    print("Eventos registrados com sucesso.")

