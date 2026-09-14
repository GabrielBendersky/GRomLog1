#Crie um script que avalie a concessão de empréstimo com base em três
#variáveis: renda_mensal (float), score (inteiro de 0 a 1000) e possui_restricao
#(booleano).
#◆ Aprovado: score maior ou igual a 700, renda_mensal a partir de 4000.00
#e sem restrições cadastrais.
#◆ Análise Manual: Se não for aprovado diretamente, mas a renda_mensal
#for de pelo menos 2500.00, sem restrições, e (score maior ou igual a 500
#ou renda_mensal superior a 6000.00).
#◆ Recusado: Qualquer outro caso.


RendaMensal = float(input("Digite sua renda mensal: "))
Score = int(input("Digite seu score: "))


# eu tinha feito - PossuiRestricao = bool(input("Você possui restrições cadastrais? (True/False): "))  


# Trata a resposta do usuário para converter em True ou False de forma correta ---- esse trecho a ia me corrigiu
RespostaRestricao = input("Você possui restrições cadastrais? (s/n): ").strip().lower()
PossuiRestricao = RespostaRestricao == 's'



if Score>= 700 and RendaMensal >= 4000.00 and not PossuiRestricao:
    print("Aprovado")
elif RendaMensal >= 2500.00 and not PossuiRestricao and (Score >= 500 or RendaMensal > 6000.00):
    print("Análise Manual")
else:
    print("Recusado")


