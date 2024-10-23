vetor = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j"]

vogais = "AEIOUaeiou"

contador = 0
while contador < 10:
    if vetor[contador] == "a" or vetor[contador] == "e" or vetor[contador] == "i" or vetor[contador] == "o" or vetor[contador] == "u":
        contador += 1
    else:
        print(vetor[contador])
        contador += 1

#-----------------------------------------------------#
        
palavra = str(input("Digite uma palavra: "))
vogais =["a", "e", "i", "o", "u"]

consoantes = 0

for letra in palavra:
    print(letra)
