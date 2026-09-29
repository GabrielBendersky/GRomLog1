# Contruir um programa onde o usuario digitara o nome e a media de dez alunos e o programa escrevera na tela o nome de todos com a media acima ou igual a seis

alunos = []
medias = []

# 1. Entrada de dados dos alunos
for i in range(10):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    media_aluno = float(input(f"Digite a média de {nome}: "))
    
    alunos.append(nome)
    medias.append(media_aluno)

# 2. Verificação e exibição dos aprovados 
print("\nAlunos com média acima ou igual a 6:")
encontrou_aprovado = False

for i in range(10):
    if medias[i] >= 6:
        print(f"- {alunos[i]} (Média: {medias[i]:.1f})")
        encontrou_aprovado = True

if not encontrou_aprovado:
    print("Nenhum aluno com média acima ou igual a 6.")