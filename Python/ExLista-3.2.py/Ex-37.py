num = int(input("Digite um numero: "))
cont = num
numero = []

while cont >= 1:
    if num % cont == 0:
        numero.append(cont)
        cont -= 1
    else:
        cont -= 1

print(numero)
if len(numero) == 2:
    print("É primo")
else:
    print("Não é primo")