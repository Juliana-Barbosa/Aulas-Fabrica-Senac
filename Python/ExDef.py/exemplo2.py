def tratartexto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

texto = "olá"
texto = tratartexto(texto)
print(texto)