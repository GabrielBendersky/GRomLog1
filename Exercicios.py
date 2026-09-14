# Programa em python que receba 3 valores em numeros reais(a,b e c) representando comprimentos de um dos lados do triangulo
# Verificar a condição de existencia geometrica a soma de dois lados quaisquer deve ser estritamente maior que o terceiro lado. 
#caso a condição seja atendida, classifique o triangulo em equilatero, isosceles ou escaleno
# se as medidas não formarem um triangulo, exiba uma mensagem de erro.



#Leitura dos lados

A = float(input('Digite o comprimento do lado a:'))
B = float(input('Digite o comprimento do lado a:'))
C = float(input('Digite o comprimento do lado a:'))



if (A+B>C) and (A+C>B) and (B+C>A):

    if A == B and B == C:
        print('equilátero')
    elif A == B or A == C or B == C:
        print ('isósceles') 
    elif A != B and A!=C and B!=A:
        print ('escaleno')

else:
    print('Erro: os valores informados não formam um triangulo')
