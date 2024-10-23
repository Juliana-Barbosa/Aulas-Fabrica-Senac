numeros = [] 
pares = []
impares = []

contador = 0
while contador < 20:
    num = int(input(f"Digite um numero inteiro ({contador + 1}/20)"))
    numeros.append(num)
    if num % 2 == 0:
     pares.append(num)
    else:
      impares.append(num)
    contador += 1

print("Lista de todos os numeros")
print(numeros)

print("Lista de numeros pares")
print(pares)

print("Lista de numeros impares")
print(impares)