#Regras do jogo Pedra, Papel e Tesoura: 

#Pedra ganha de Tesoura (porque a pedra quebra a tesoura).

#Tesoura ganha de Papel (porque a tesoura corta o papel).

#Papel ganha de Pedra (porque o papel embrulha/cobre a pedra).





#jogadores

jogador1 = input("Jogador 1, escolha Pedra, Papel ou Tesoura: ")
jogador2 = input("Jogador 2, escolha Pedra, Papel ou Tesoura: ")
jogadas = ['Pedra', 'Papel', 'Tesoura']


if (jogador1 not in jogadas or jogador2 not in jogadas):

print('jogada invalida'):


#verificando o vencedor


if jogador1 == jogador2:
    print("Empate!")


#vitoria do jogador 1


elif (jogador1 == "Pedra" and jogador2 == "Tesoura")    \
   or (jogador1 == "Tesoura" and jogador2 == "Papel")   \
   or (jogador1 == "Papel" and jogador2 == "Pedra"):
    print("Jogador1 Venceu!")


#vitoria do jogador 2 caso nenhuma das condições acima seja verdadeira
else:
    print("Jogador2 Venceu!")

    
    