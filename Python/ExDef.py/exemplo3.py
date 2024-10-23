def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

produtos = ["maçã", "uva", "tomate", "limão"]

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

print(produtos)
