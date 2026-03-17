def imprimir_tabla_transiciones(afd, alfabeto):

    estados = afd["estados"]
    transiciones = afd["transiciones"]
    nombres = afd["nombres"]
    inicial = afd["estado_inicial"]
    finales = afd["aceptacion"]

    print("\nTABLA DE TRANSICIÓN\n")

    encabezado = "Estado\t" + "\t".join(alfabeto)
    print(encabezado)

    for estado in estados:

        nombre_estado = nombres[estado]

        if estado == inicial:
            nombre_estado = "->" + nombre_estado

        if estado in finales:
            nombre_estado = "*" + nombre_estado

        fila = nombre_estado

        for simbolo in alfabeto:

            if simbolo in transiciones[estado]:
                destino = transiciones[estado][simbolo]
                fila += "\t" + nombres[destino]
            else:
                fila += "\t-"

        print(fila)