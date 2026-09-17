
# limitador 4

#for i in range(0, 5):  
#  if i < 5:
#     print(i)


#como o for funciona 50 entrada -1 limitador, -2 passadas
#for i in range(50, -1, -2):
#    print(i)


#numero = int(input("Digite um número: "))
#for i in range(numero, -1, -2):
 #   if i % 2 == 0:
  #      print(i)



#construa uma pagina onde o usuario digitara um valor e o programa mostrara na tela a tabuada de multiplicação deste numero.
numero = int(input("Digite um número: "))   
for i in range(0, 11):
    resultado = numero * (i+1)
    print(f"{numero} x {i+1} = {resultado}")




i = 0
while i < 10:
    print(f"{numero} x {i+1} = {numero * (i+1)}")
    i += 1
