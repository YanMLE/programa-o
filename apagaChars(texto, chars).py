def apagaChars(texto, chars):
    resultado = ''
    for i in texto:
        if i not in chars:
            resultado += i
    print(resultado)