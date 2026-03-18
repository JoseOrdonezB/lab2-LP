def imprimir_tabla_transiciones(afd, alfabeto):
    estados = afd["estados"]
    transiciones = afd["transiciones"]
    nombres = afd["nombres"]
    inicial = afd["estado_inicial"]
    finales = afd["aceptacion"]

    print("\nTABLA DE TRANSICIÓN")

    encabezado = ["Estado"] + list(alfabeto)
    print(" | ".join(encabezado))
    print("-" * (len(" | ".join(encabezado)) + 8))

    ordenados = [inicial] + [e for e in estados if e != inicial]

    for estado in ordenados:
        nombre_estado = nombres[estado]

        if estado == inicial:
            nombre_estado = "->" + nombre_estado

        if estado in finales:
            nombre_estado = "*" + nombre_estado

        fila = [nombre_estado]

        for simbolo in alfabeto:
            if simbolo in transiciones[estado]:
                destino = transiciones[estado][simbolo]
                fila.append(nombres[destino])
            else:
                fila.append("-")

        print(" | ".join(fila))