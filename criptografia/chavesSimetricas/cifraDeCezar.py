def criptografar(texto, numeroDaChave):
    resultado = "" # String vazia que irá ser incrementada
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            resultado += chr((ord(char) + numeroDaChave-65)%26 + 65)
        else:
            resultado += chr((ord(char)+ numeroDaChave-97)%26+97)
    return resultado

def descriptografar(texto, numeroDaChave):
    texto = texto.upper()
    biblioteca = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    for letra in texto:
        if letra in texto:
            indexDaLetra = (biblioteca.find(letra) - numeroDaChave)%len(biblioteca)
            resultado += biblioteca[indexDaLetra]
        else:
            resultado += letra
    return resultado
print(criptografar("ABCDE", 3))
print(descriptografar((criptografar("ABCDE", 3)), 3))