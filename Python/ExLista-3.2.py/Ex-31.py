salarioinicial = 4000
aumentoinicial = 1.5 / 100

anoatual = 2024

salarioatual = salarioinicial
aumentoatual = aumentoinicial

ano = 2020

while ano <= anoatual:
    salarioatual += salarioatual * aumentoatual
    aumentoatual *= 2
    ano += 1

print(f"O salário atual do funcionario em {anoatual} é: R${salarioatual:.2f} ")
