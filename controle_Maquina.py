#Um sistema de controle de maquinário pesado deve autorizar a operação
#com base em: cargo (string: "operador" ou "supervisor"), hora_atual (inteiro
#de 0 a 23) e chave_emergencia (booleano). O acesso deve ser concedido se:
#◆ A chave_emergencia estiver ativa (True), independentemente de
#qualquer outra variável; OU
#◆ O usuário for "supervisor"; OU
#◆ O usuário for "operador" E a hora_atual estiver entre 8 e 17 (inclusive).
#◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado".



# Coleta de dados 
cargo_usuario = input("Digite o cargo (operador/supervisor): ")
hora_usuario = int(input("Digite a hora atual (0 a 23): "))
chave_emergencia = input("A chave de emergência está ativa? (s/n): "). strip().lower() == "S"



def autorizar_operacao(cargo : str, hora_atual: int , chave_emergencia: bool) -> str: 
    cargo = cargo.lower()

# Condição para liberar maquina
    if chave_emergencia or cargo == "supervisor" or (cargo == "operador" and 8 <= hora_atual <= 17):
        return "Acesso Permitido"

    return "Acesso Bloqueado"



# Exibir resultado
resultado = autorizar_operacao(cargo_usuario, hora_usuario, chave_emergencia)
print(f"\nStatus: {resultado}")


