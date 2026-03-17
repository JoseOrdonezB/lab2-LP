from src.regex import preparar_regex
from src.afd_directo import construir_afd_directo
from src.transiciones import imprimir_tabla_transiciones
from src.simulacion import simular_afd, verificar_cadena

regex = input("Ingrese la expresión regular: ")

regex_preparada, alfabeto = preparar_regex(regex)

print("\nRegex preparada:", regex_preparada)
print("Alfabeto:", alfabeto)

afd = construir_afd_directo(regex_preparada, alfabeto)

print("\nPOSTFIJO:", afd["postfijo"])

print("\nFOLLOWPOS")
for pos in sorted(afd["followpos"]):
    print(pos, "->", sorted(afd["followpos"][pos]))

print("\nESTADOS")
for estado in afd["estados"]:
    nombre = afd["nombres"][estado]
    print(nombre, "=", set(estado))

print("\nESTADO INICIAL")
print(afd["nombres"][afd["estado_inicial"]])

print("\nESTADOS DE ACEPTACION")
for estado in afd["aceptacion"]:
    print(afd["nombres"][estado], "=", set(estado))

print("\nTRANSICIONES")
for estado, trans in afd["transiciones"].items():

    nombre = afd["nombres"][estado]

    for simbolo, destino in trans.items():
        print(nombre, "--", simbolo, "-->", afd["nombres"][destino])

imprimir_tabla_transiciones(afd, alfabeto)

# Verificación de cadenas
while True:

    cadena = input("\nIngrese una cadena (o escriba 'salir'): ")

    if cadena.lower() == "salir":
        print("Finalizando programa.")
        break

    pertenece = verificar_cadena(afd, cadena, alfabeto)

    if pertenece:
        print("\nResultado final: CADENA ACEPTADA ✅")
    else:
        print("\nResultado final: CADENA RECHAZADA ❌")

    # Recorrido detallado
    print("\n--- Detalle de la simulación ---")
    simular_afd(afd, cadena, alfabeto)