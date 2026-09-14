# como achar o menor valor entre dois numeros



#passo1 >> ter 2 numeros

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))


# passo n2 >> teste condicional 5


if n1 < n2:
    print (f"{n1} é menor do que o {n2}")
elif n1 == n2 :
    print(f"ambos os numeros são iguais")
else:
    print(f"{n2} é menor do que o {n1}")
