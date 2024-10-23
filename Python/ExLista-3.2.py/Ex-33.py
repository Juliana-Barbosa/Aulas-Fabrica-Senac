vetor = []
print ("Digite os dez números inteiros")
cont = 0
while cont < 10:
    num = int(input(f"Posição {cont + 1}: "))
    vetor.append(num)
    cont += 1

novovalor = int(input("Digite um novo valor: "))

cont = 0 
while cont < 10:
    if vetor[cont] == novovalor:
        print(f"O valor {novovalor} está presente no vetor")
        break
    cont += 1
else:
    print(f"O valor {novovalor} não esta presente no vetor")
    