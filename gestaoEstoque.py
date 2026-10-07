#O programa deve preencher duas listas paralelas de tamanho fixo (6 #posições): uma contendo o código numérico de cada produto e outra contendo o respectivo saldo em estoque.
cod_numerico = []
saldo_estoque = []


for i in range(6):
    codigo = int(input(f"Digite o código numérico do produto: "))
    saldo = int(input(f"Digite o saldo em estoque do produto:"))
    
    
    cod_numerico.append(codigo)
    saldo_estoque.append(saldo)
    

#Solicite ao operador o valor do "Estoque Mínimo de Segurança" (um número inteiro único para a verificação de toda a linha).

estoque_minimo = int(input("Digite o valor do Estoque Mínimo de Segurança: "))


#Realize uma varredura nas estruturas e identifique:
indice_menor_saldo = 0
indice_maior_saldo = 0
contador = 0



for produto in range(6):

    if saldo_estoque[produto] < estoque_minimo:
        print(f"Produto com código {cod_numerico[produto]} está abaixo do estoque mínimo. Quantidade atual: {saldo_estoque[produto]}")
        contador += 1

#Quais produtos estão com saldo estritamente abaixo do estoque mínimo, exibindo seu código e quantidade atual;

    if saldo_estoque[produto] < saldo_estoque[indice_menor_saldo]:
        indice_menor_saldo = produto

    if saldo_estoque[produto] > saldo_estoque[indice_maior_saldo]:
        indice_maior_saldo = produto

#O código e a quantidade do item que possui o menor saldo absoluto no almoxarifado;
print(f"Produto com código {cod_numerico[indice_menor_saldo]} possui o menor saldo. Quantidade: {saldo_estoque[indice_menor_saldo]}")

#O código e a quantidade do item com maior saldo absoluto.
print(f"Produto com código {cod_numerico[indice_maior_saldo]} possui o maior saldo. Quantidade: {saldo_estoque[indice_maior_saldo]}")



#Caso nenhum produto esteja abaixo do estoque de segurança, exiba a mensagem "Estoque Operando em Parâmetros Normais".

if contador == 0:
    print("Estoque Operando em Parâmetros Normais")


