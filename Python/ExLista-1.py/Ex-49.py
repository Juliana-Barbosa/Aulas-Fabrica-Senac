lata = 350
garrafa600 = 600
garrafa2l = 2000
qlata = float(input("Digite a quanditade compradas: "))
qgarrafa600 = float(input("Digite a quanditade compradas: "))
qgarrafa2l = float(input("Digite a quanditade compradas: "))

total = (qlata * lata / 1000) + (qgarrafa600 * garrafa600 / 1000) + (qgarrafa2l * garrafa2l / 1000)

print ("o comerciante comprou ", total )