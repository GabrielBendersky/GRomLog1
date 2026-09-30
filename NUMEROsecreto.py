import random

numero_secreto = random.randint(1, 500)
tentativas = 5
pontos = 0

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Tente adivinhar o número entre 1 e 500!")


while tentativas > 0:
    palpite = int(input("\nDigite seu palpite: "))
    tentativas -= 1  # Diminui 1 tentativa a cada palpite

    if palpite == numero_secreto:
        print(f"\nvocê é inteligente mesmo,brabo {numero_secreto}!")
        if tentativas == 1:
            pontos += 100
        elif  tentativas == 5:
            pontos += 10
        else: 
            pontos += (100 - tentativas * 25)

        break
    elif palpite < numero_secreto:
        print("Tente um número MAIOR!")
    else:
        print("Tente um número MENOR!")

    if tentativas > 0:
        print(f"Você ainda tem {tentativas} chance (s).")
    else:
        print(f"\nSeu animal, você errou tudo !  O número secreto era {numero_secreto} molezinha, mamão com açúcar.")


if pontos >= 200:
    print ('Sabe muito, faturou {pontos}')

elif 100 < pontos <200 :
    print (f'Até que não errou feio, pode tentar jogar no bixo! seus pontos foram {pontos}')

else : 
    print(f'desiste irmão você é muito ruim {pontos}')
    




        