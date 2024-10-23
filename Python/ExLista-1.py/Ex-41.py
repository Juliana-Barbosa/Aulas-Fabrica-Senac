valortotal =  float(input("Digite o valor da compra: "))
desconto = valortotal*0.9
parcela = valortotal/3
comissaovista = desconto * 0.05
comissaoparcela = valortotal * 0.05

print ("total a pagar com desconto de 10%: ", desconto)
print ("total a pagar em 3x é: ", parcela)
print ("total a pagar de comissão à vista é: ", comissaovista)
print ("total a pagar de comissão de parcela: ", comissaoparcela)