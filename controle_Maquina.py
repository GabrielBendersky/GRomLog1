#Um sistema de controle de maquinário pesado deve autorizar a operação
#com base em: cargo (string: "operador" ou "supervisor"), hora_atual (inteiro
#de 0 a 23) e chave_emergencia (booleano). O acesso deve ser concedido se:
#◆ A chave_emergencia estiver ativa (True), independentemente de
#qualquer outra variável; OU
#◆ O usuário for "supervisor"; OU
#◆ O usuário for "operador" E a hora_atual estiver entre 8 e 17 (inclusive).
#◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado".


def autorizar_operacao(cargo : str, hora_atual: int , chave_emergencia: bool) -> str: 
    cargo = cargo.lower()

# Condições de liberação 
    if chave_emergencia or cargo == "supervisor" or (cargo == "operador" and 8 <= hora_atual <= 17):
        return "Acesso Permitido"

    return "Acesso Bloqueado"


# Coleta de dados pelo terminal
cargo_usuario = input("Digite o cargo (operador/supervisor): ")
hora_usuario = int(input("Digite a hora atual (0 a 23): "))
emergencia_usuario = input("A chave de emergência está ativa? (s/n): ").strip().lower() == "s"
# Chamada da função e exibição
resultado = autorizar_operacao(cargo_usuario, hora_usuario, emergencia_usuario)
print(f"\nStatus: {resultado}")


