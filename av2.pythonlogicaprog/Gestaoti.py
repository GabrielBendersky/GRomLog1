# Sistema de Gestão de Chamados Técnicos (Service Desk) (2.py) [Valor: 20
# Pontos]
# A central de suporte de TI necessita de um módulo de console para registro, triagem e controle de
# chamados técnicos internos. Desenvolva uma solução estruturada em Python utilizando modularização
# com funções, listas e dicionários.
# ● Regras de Negócio e Requisitos Técnicos:
# a. Estrutura de Dados: Armazenar chamados em lista de dicionários com chaves: id (inteiro
# incremental a partir de 1), usuario (texto), descricao (texto), prioridade ('BAIXA', 'MEDIA'
# ou 'ALTA') e status (iniciado automaticamente como 'ABERTO').
# b. Validação com while: A prioridade deve ser validada via laço while, aceitando apenas
# 'BAIXA', 'MEDIA' ou 'ALTA', solicitando redigitação imediata em caso de erro.
# c. Funções Obrigatórias: Implementar obrigatoriamente as seguintes funções estruturadas:
# i. adicionar_chamado(lista, id, usuario, descricao, prioridade): recebe os dados,
# monta o dicionário e insere na lista;
# ii. listar_chamados(lista, filtro_prioridade=None): percorre e imprime os chamados
# (com filtro opcional de prioridade ou todos caso None);
# iii. encerrar_chamado(lista, id): localiza pelo ID e altera status para 'CONCLUÍDO' (ou
# avisa caso não exista);
# iv. obter_total_abertos(lista): retorna a quantidade total de chamados ainda com
# status 'ABERTO'.
# d. Menu de Console: Construir menu interativo em console com laço contínuo: 1 - Novo
# Chamado, 2 - Listar Todos, 3 - Listar por Prioridade, 4 - Encerrar Chamado e 0 - Sair.
# Restrição Técnica: Funções com parâmetros e retornos bem definidos. Lógica de busca e
# acumulação via laços for e condicionais if.




#adicionar_chamado(lista, id, usuario, descricao, prioridade)
def add_chamado(lista, id, usuario, descricao, prioridade):
    """Adiciona um novo chamado à lista de chamados."""
    chamado = {
        "id": id,
        "usuario": usuario,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "ABERTO"
    }
    lista.append(chamado)
    return chamado



#listar_chamados(lista, filtro_prioridade=None)
def listar_chamados(lista, filtro_prioridade=None):
    encontrados = 0
    for chamado in lista:
        if filtro_prioridade:
            print(f"LISTA DE CHAMADOS COM PRIORIDADE {filtro_prioridade}:")
        else:
            print("LISTA DE TODOS OS CHAMADOS:")
        print("=" * 81)
        print(f"{'ID':<6} | {'USUARIO':<20} | {'DESCRICAO':<30} | {'PRIORIDADE':<10} | {'STATUS':<10}")
        print("=" * 81)
        for chamado in lista:
            if filtro_prioridade is None or chamado["prioridade"] == filtro_prioridade:
                print(f"{chamado['id']:<6} | {chamado['usuario']:<20} | {chamado['descricao']:<30} | {chamado['prioridade']:<10} | {chamado['status']:<10}")
                encontrados += 1
        if encontrados == 0:
            print("Nenhum chamado encontrado com a prioridade especificada.")

        print("=" * 81)
        return encontrados


#encerrar_chamado(lista, id)

def encerrar_chamado(lista, id):
    """Busca o chamado pelo ID e altera seu status para 'CONCLUÍDO'."""
    for chamado in lista:
        if chamado["id"] == id:
            if chamado["status"] == "CONCLUÍDO":
                print(f"Aviso: O chamado #{id} já está encerrado.")
            else:
                chamado["status"] = "CONCLUÍDO"
                print(f"Chamado #{id} encerrado com sucesso (Status: CONCLUÍDO).")
            return True
    print(f"Erro: Chamado com ID #{id} não foi encontrado.")
    return False


# obter_total_abertos(lista): retorna a quantidade total de chamados ainda com  status 'ABERTO'.
def obter_total_abertos(lista):
    """Conta e retorna a quantidade de chamados com status 'ABERTO'."""
    total_abertos = 0
    for chamado in lista:
        if chamado["status"] == "ABERTO":
            total_abertos += 1
    return total_abertos


# b) Validação com while: A prioridade deve ser validada via laço while, aceitando apenas BAIXA', 'MEDIA' ou 'ALTA', 

def validar_prioridade():
    """Solicita ao usuário a prioridade do chamado e valida a entrada."""
    while True:
        prioridade = input("Digite a prioridade do chamado (BAIXA, MEDIA, ALTA): ").strip().upper()
        if prioridade in ["BAIXA", "MEDIA", "ALTA"]:
            return prioridade
        else:
            print("Erro: Prioridade inválida. Digite apenas BAIXA, MEDIA ou ALTA.")


def executar_sistema():
    chamados = []
    proximo_id = 1

    #Menu de Console: Construir menu interativo 
   
    while True:
        aberto = obter_total_abertos(chamados)
        print("\nSistema de Gestão de Chamados Técnicos (Service Desk)")
        print("1 - Novo Chamado")
        print("2 - Listar Todos")
        print("3 - Listar por Prioridade")
        print("4 - Encerrar Chamado")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            print("\n--- Novo Chamado ---")
            usuario = input("Digite o nome do usuário: ").strip()
            descricao = input("Digite a descrição do chamado: ").strip()
            prioridade = validar_prioridade()
            novo_chamado = add_chamado(chamados, proximo_id, usuario, descricao, prioridade)
            print(f"Chamado #{novo_chamado['id']} adicionado com sucesso (Status: {novo_chamado['status']}).")
            proximo_id += 1

        elif opcao == "2":
            print("\n--- Listar Todos os Chamados ---")
            listar_chamados(chamados)

        elif opcao == "3":
            print("\n--- Listar Chamados por Prioridade ---")
            prioridade = validar_prioridade()
            listar_chamados(chamados, filtro_prioridade=prioridade)

        elif opcao == "4":
            print("\n--- Encerrar Chamado ---")
            try:
                id_encerrar = int(input("Digite o ID do chamado a ser encerrado: ").strip())
                encerrar_chamado(chamados, id_encerrar)
            except ValueError:
                print("Erro: ID inválido. Digite um número inteiro.")

        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Erro: Opção inválida. Digite apenas 1, 2, 3, 4 ou 0.")


if __name__ == "__main__":
    executar_sistema()
            