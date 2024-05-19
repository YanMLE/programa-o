def mdc_lista(lista):
    resultado = lista[0]
    for num in lista[1:]:
        while num:
            resultado, num = num, resultado % num
    print(f"O MDC de {lista} é {resultado}")

