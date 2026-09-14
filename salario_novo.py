#Uma empresa vai dar um reajuste salarial com base no tempo de serviço e na nota de avaliação do funcionário (de 1 a 10).
#Aumento de 15%: Funcionários com mais de 5 anos de empresa E nota de avaliação maior ou igual a 8.
#Aumento de 10%: Funcionários que NÃO atingiram a regra acima, mas têm pelo menos 2 anos de empresa 
#   OU nota de avaliação maior ou igual a 7.
#  Aumento de 5%: Todos os outros casos.
#Objetivo: Calcule e exiba o valor do novo salário reajustado.


TempoServico = int(input("Digite o tempo de serviço (em anos): "))
NotaAvaliacao = float(input("Digite a nota de avaliação (de 1 a 10): "))

if TempoServico > 5 and NotaAvaliacao >= 8:
    aumento = 0.15
elif TempoServico >= 2 or NotaAvaliacao >= 7:
    aumento = 0.10
else:
    aumento = 0.05  

SalarioAtual = float(input("Digite o salário atual: "))
NovoSalario = SalarioAtual * (1 + aumento)
print(f"Seu salário foi reajustado para: R$ {NovoSalario:.2f}")
