pao = 0.12
broa = 1.50
quantidadeP = float(input("Digite o valor dos paes vendidos: "))
quantidadeB = float(input("Digite o valor das broas vendidas: "))
total = (quantidadeP * pao) + (quantidadeB * broa)
valorpoupanca = total * 0.10

print ("total arrecadado com venda dos paes e boas: ", total)
print ("valor  a ser guardado na conta poupança ", valorpoupanca)