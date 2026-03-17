def simular_afd(afd, cadena, alfabeto):

    estado_actual = afd["estado_inicial"]
    transiciones = afd["transiciones"]
    aceptacion = afd["aceptacion"]

    print("\nSIMULACIÓN")
    print("Estado inicial:", afd["nombres"][estado_actual])

    for simbolo in cadena:

        if simbolo not in alfabeto:
            print(f"Símbolo '{simbolo}' no pertenece al alfabeto.")
            return False

        if simbolo not in transiciones[estado_actual]:
            print("No existe transición.")
            return False

        estado_actual = transiciones[estado_actual][simbolo]
        print(f"Con '{simbolo}' →", afd["nombres"][estado_actual])

    if estado_actual in aceptacion:
        print("\nResultado: CADENA ACEPTADA ✅")
        return True
    else:
        print("\nResultado: CADENA RECHAZADA ❌")
        return False
    
def verificar_cadena(afd, cadena, alfabeto):

    estado_actual = afd["estado_inicial"]
    transiciones = afd["transiciones"]
    aceptacion = afd["aceptacion"]

    for simbolo in cadena:

        if simbolo not in alfabeto:
            return False

        if simbolo not in transiciones[estado_actual]:
            return False

        estado_actual = transiciones[estado_actual][simbolo]

    return estado_actual in aceptacion