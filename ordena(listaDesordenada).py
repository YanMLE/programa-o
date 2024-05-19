def ordena(listaDesordenada):
    for i in range(1, len(listaDesordenada)):
        chave = listaDesordenada[i]
        j = i - 1
        while j >= 0 and chave < listaDesordenada[j]:
            listaDesordenada[j + 1] = listaDesordenada[j]
            j -= 1
        listaDesordenada[j + 1] = chave
    resultado = listaDesordenada
    print(f"Lista ordenada: {resultado}")
