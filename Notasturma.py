#A secretaria de uma escola técnica disponibilizou o arquivo notas_turma.csv
#com as colunas matricula, aluno, nota1 e nota2.
#leia esses registros e calcule a média aritmética de cada aluno.
#Se a média final for maior ou igual a 7.0, o aluno recebe a situação "Aprovado", caso contrário, recebe a situação "Reprovado".
# O programa deve gerar o arquivo boletim_final.csv contendo as notas originais, a média final arredondada para uma casa decimal e a situação acadêmica calculada.

import csv


#criar arquivo csv notas_turma.csv ao final do script 
dados_exemplo = """matricula;aluno;nota1;nota2
202601;Lucas Silva;8.5;7.0
202602;Beatriz Ramos;5.0;6.5
202603;Carlos Drummond;9.0;9.5
202604;Fernanda Dias;4.0;5.0
202605;Rodrigo Prado;7.0;7.0"""


with open("notas_turma.csv", "w", newline="", encoding="utf-8") as arquivo_exemplo:
    arquivo_exemplo.write(dados_exemplo)



#Processa as notas, calcula a média e define a situação acadêmica

with open("notas_turma.csv", "r", encoding="utf-8") as arquivo_entrada, \
     open("boletim_final.csv", "w", newline="", encoding="utf-8") as arquivo_saida:


     leitor_csv = csv.DictReader(arquivo_entrada, delimiter=';')

#Adiciona as novas colunas no cabeçalho

     campos_saida = leitor_csv.fieldnames + ['media', 'situacao']
     escritor_csv = csv.DictWriter(arquivo_saida, fieldnames=campos_saida, delimiter=';')
     escritor_csv.writeheader()


     for linha in leitor_csv:
        nota1 = float(linha['nota1'])
        nota2 = float(linha['nota2'])

#Cálculo da média aritmética arredondada para 1 casa decimal
        media = round((nota1 + nota2) / 2, 1)

#Definição da situação acadêmica
        if media >= 7.0:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

#Adiciona os dados processados ao arquivo de saída
        linha['media'] = media
        linha['situacao'] = situacao

        escritor_csv.writerow(linha)

print("Processamento concluído. O arquivo boletim_final.csv foi gerado com sucesso.")
