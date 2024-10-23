valornormal= 32.50
valorextra = 44.50

normais = float(input("Digite a quanditade de horas normais: "))
extras = float(input("Digite a quanditade de horas extras: "))
salariobruto = (normais * valornormal) + (extras * valorextra)

desconto = salariobruto  * 0.11
liquido =  salariobruto - desconto
print ("salario bruto: ", salariobruto )
print ("salario liquido: ", liquido )
