#Exercício 1: Validador de Acesso (Iniciante)
#Crie um programa que determine se uma pessoa pode entrar em um brinquedo de parque de diversões.
#Critérios para permitir o acesso: A pessoa deve ter pelo menos 12 anos E altura mínima de 1.40m.
#Resultado: Imprima "Acesso liberado" se cumprir ambos os requisitos, ou "Acesso negado" caso contrário.
#Dica: Peça a idade (int) e a altura (float) usando input().


Idade = int(input("Digite sua idade: "))
Altura = float(input("Digite sua altura (em metros): "))

if Idade >= 12 and Altura >= 1.40:
    print("Acesso liberado")
else:
    print("Acesso negado")  
    