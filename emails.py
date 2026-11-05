# Um formulário web despadronizado gerou um arquivo de texto bruto chamado emails_brutos.txt com e-mails digitados pelos usuários.

#Esse arquivo contém espaçamentos indesejados nas pontas, caracteres maiúsculos misturados e linhas vazias acidentais.

# Escreva um script em Python que leia esse arquivo linha por linha, descarte linhas em branco, converta todos os e-mails válidos para letras minúsculas (lowercase),

#remova espaços extras nas pontas e salve a lista limpa e padronizada em um novo arquivo chamado emails_padronizados.txt.


with open("emails_brutos.txt", "r", encoding="utf-8") as arquivo_entrada, \
     open("emails_padronizados.txt", "w", encoding="utf-8") as arquivo_saida:

    for linha in arquivo_entrada:
        # Remover espaços extras nas pontas e converter para minúsculas
        email = linha.strip().lower()
        
        # Descartar linhas em branco
        if email:
            arquivo_saida.write(email + "\n")

print("Arquivo emails_padronizados.txt gerado com sucesso.")
