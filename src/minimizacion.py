def minimizar_afd(afd, alfabeto):

    estados = afd["estados"]
    transiciones = afd["transiciones"]
    inicial = afd["estado_inicial"]
    finales = set(afd["aceptacion"])

    no_finales = set(estados) - finales
    particiones = []

    if finales:
        particiones.append(set(finales))

    if no_finales:
        particiones.append(set(no_finales))

    cambio = True

    while cambio:

        cambio = False
        nuevas_particiones = []

        for grupo in particiones:

            firmas = {}

            for estado in grupo:

                firma = []

                for simbolo in alfabeto:

                    if simbolo in transiciones[estado]:
                        destino = transiciones[estado][simbolo]

                        indice = None
                        for i,p in enumerate(particiones):
                            if destino in p:
                                indice = i
                                break

                        firma.append(indice)

                    else:
                        firma.append(None)

                firma = tuple(firma)

                if firma not in firmas:
                    firmas[firma] = set()

                firmas[firma].add(estado)

            nuevas_particiones.extend(firmas.values())

            if len(firmas) > 1:
                cambio = True

        particiones = nuevas_particiones

    nuevos_estados = [frozenset(p) for p in particiones]

    estado_a_grupo = {}

    for grupo in nuevos_estados:
        for estado in grupo:
            estado_a_grupo[estado] = grupo

    nuevas_transiciones = {}

    for grupo in nuevos_estados:

        representante = next(iter(grupo))
        nuevas_transiciones[grupo] = {}

        for simbolo in alfabeto:

            if simbolo in transiciones[representante]:

                destino = transiciones[representante][simbolo]
                nuevas_transiciones[grupo][simbolo] = estado_a_grupo[destino]

    nuevo_inicial = estado_a_grupo[inicial]

    nuevos_finales = set()

    for grupo in nuevos_estados:
        if any(e in finales for e in grupo):
            nuevos_finales.add(grupo)

    nombres = {estado: f"M{i}" for i,estado in enumerate(nuevos_estados)}

    return {
        "estados": nuevos_estados,
        "transiciones": nuevas_transiciones,
        "estado_inicial": nuevo_inicial,
        "aceptacion": nuevos_finales,
        "nombres": nombres
    }