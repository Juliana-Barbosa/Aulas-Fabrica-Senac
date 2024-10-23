numero = int(input("Digite um número inteiro (ou um número negativo para sair): "))

if numero >= 0:
    menor = numero
    maior = numero
    
    while numero >= 0:
        numero = int(input("Digite um número inteiro (ou um número negativo para sair): "))
        
        if numero >= 0:
            if numero < menor:
                menor = numero
            if numero > maior:
                maior = numero
    
    print(f"O menor número lido foi: {menor}")
    print(f"O maior número lido foi: {maior}")
else:
    print("Nenhum número válido foi lido.")

#----------------------------------------------------------------------------------------------#
    
