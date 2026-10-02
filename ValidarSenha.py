
senha=0



print ("=== SISTEMA DE AUTENTICAÇÃO ===")
print ("======ROMER REGISTRATION======")


#Cadastro da senha 
while senha < 1000 or senha > 9999:
    senha = int(input("Digite uma senha numérica de 4 dígitos (entre 1000 e 9999): "))
    if senha < 1000 or senha > 9999:
        print("Senha inválida. Tente novamente.")


#REGRAS E PRINT

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


#Liberação de acesso 

if acesso_liberado:
    print("Acesso liberado! Inicializando o sistema...")
    for i in range(5, 0, -1):
        print(f"{i}...")
    print("Sistema inicializado com sucesso!")
else :
    print("Acesso negado. Sua conta foi bloqueada.")