# Crie um sistema de autenticação de terminal que valida a segurança da senha cadastrada e gerencia o acesso do usuário. 
#Regras de Negócio: 
#Primeiro, o usuário define uma senha numérica de 4 dígitos. Use um loop while que continue solicitando até que o valor digitado esteja rigorosamente entre 1000 e 9999. 
#Em seguida, o sistema entra em modo de bloqueio e pede a confirmação da senha para liberar o sistema, permitindo até 3 tentativas via loop while. 
#Dentro do processo de tentativa:
#Se a senha estiver correta: encerre imediatamente o loop de tentativas. 
#Se estiver incorreta: informe quantas chances ainda restam usando if/elif/else
#Se o acesso for liberado com sucesso, use um loop for para simular uma contagem regressiva de inicialização do sistema (de 5 até 1). 
#Se as 3 tentativas falharem, exiba a mensagem de conta bloqueada. 



senha = 0


#Cadastro da senha 

while senha < 1000 or senha > 9999:
    senha = int(input("Digite uma senha numérica de 4 dígitos (entre 1000 e 9999): "))
    if senha < 1000 or senha > 9999:
        print("Senha inválida. Tente novamente.")

# bloqueio

tentativas = 3
acesso_liberado = False

while tentativas > 0:
    senha_tentativa = int(input("Digite a senha para liberar o sistema: "))
    if senha_tentativa == senha:
        acesso_liberado = True
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Você tem {tentativas} tentativa(s) restante(s).")
        else:
            print("Senha incorreta. Sua conta foi bloqueada.")
#Liberação

if acesso_liberado:
    print("Acesso liberado! Inicializando o sistema...")
    for i in range(5, 0, -1):
        print(f"{i}...")
    print("Sistema inicializado com sucesso!")
else :
    print("Acesso negado. Sua conta foi bloqueada.")



