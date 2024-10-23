salariobase = int(input("Digite o valor do salario: "))
gratificacao = salariobase * 0.05
imposto = salariobase * 0.07
salarioreceber = salariobase + gratificacao - imposto 

print("o salario a receber é: ", salarioreceber)

