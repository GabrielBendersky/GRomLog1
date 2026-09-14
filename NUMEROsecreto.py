import random

numero_secreto = random.randint(1, 500)
tentativas = 5

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Tente adivinhar o número entre 1 e 500!")
print(f"Você tem {tentativas} chances.")

while tentativas > 0:
    palpite = int(input("\nDigite seu palpite: "))
    tentativas -= 1  # Diminui 1 tentativa a cada palpite

    if palpite == numero_secreto:
        print(f"\nParabéns! Você acertou o número {numero_secreto}!")
        break
    elif palpite < numero_secreto:
        print("Tente um número MAIOR!")
    else:
        print("Tente um número MENOR!")

    if tentativas > 0:
        print(f"Você ainda tem {tentativas} chance (s).")
    else:
        print(f"\nSeu animal, você errou tudo !  O número secreto era {numero_secreto} molezinha, mamão com açúcar.")



        