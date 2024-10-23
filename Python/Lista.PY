lista = [6.5,5,19,8,3,34,5.8,45]

print(lista)
lista.pop()
lista.pop()

print(lista)

lista.append(5)
lista.append(89)
lista.append(34)
print(lista)

lista.insert(6,66)
print(lista)

lista.pop(-3)
print(lista)

print(len(lista))
print(sum(lista))

media = sum(lista) / len(lista)
print (media)
medianova = round(media)
print (medianova)

lista.sort(reverse=True)
print (lista)

print (min(lista))
print (max(lista))