def mmc(lista):
    resultado = lista[0]
    for num in lista[1:]:
        a, b = resultado, num
        while b:
            a, b = b, a % b
        mdc = a
        resultado = (resultado * num) // mdc
    
    print(f"O MMC de {lista} é {resultado}")
