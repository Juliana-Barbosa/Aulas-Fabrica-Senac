valordia = 30
dias = int(input("Digite o numero de dias trabalhados: "))
valorbruto = valordia * dias
impostorenda = valorbruto * 0.08
valorliquido = valorbruto - impostorenda

print("a quantidade liquida a ser paga é : ", valorliquido)