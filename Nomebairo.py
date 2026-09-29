#usuario digitara o nome e o bairro e o de dez pessoas, o programa ira mostrar o nome e o bairro de cada pessoa digitada e no final mostrara o nome e o bairro em ordem alfabetica

cadastro = []
for i in range(10):
    nome = input("Digite o nome da pessoa: ")
    bairro = input("Digite o bairro da pessoa: ")
    cadastro.append([nome, bairro])

# Exibir os dados cadastrados
print("\nDados cadastrados:")
for nome, bairro in cadastro:
    print(f"Nome: {nome}, Bairro: {bairro}")

# Ordenar os dados por nome
cadastro.sort()   #opção de ordenação key=lambda x: x[0]

# Exibir os dados em ordem alfabetica
print("\nDados em ordem alfabetica:")
for nome, bairro in cadastro:
    print(f"Nome: {nome}, Bairro: {bairro}")


