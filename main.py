from src.regex import preparar_regex
from src.afd_directo import construir_afd_directo
from src.minimizacion import minimizar_afd
from src.transiciones import imprimir_tabla_transiciones

regex = input("Ingrese la expresión regular: ")

regex_preparada, alfabeto = preparar_regex(regex)

afd = construir_afd_directo(regex_preparada, alfabeto)
afd_min = minimizar_afd(afd, alfabeto)

estados_directo = len(afd["estados"])
trans_directo = sum(len(v) for v in afd["transiciones"].values())

estados_min = len(afd_min["estados"])
trans_min = sum(len(v) for v in afd_min["transiciones"].values())

# expresión regular para probar: (a|b)*abb(a|b)*

print("\nRESULTADO DE MINIMIZACIÓN")

print("\nAFD DIRECTO")
imprimir_tabla_transiciones(afd, alfabeto)
print(f"\nCantidad de estados: {estados_directo}")
print(f"Cantidad de transiciones: {trans_directo}")

print("\nAFD MINIMIZADO")
imprimir_tabla_transiciones(afd_min, alfabeto)
print(f"\nCantidad de estados: {estados_min}")
print(f"Cantidad de transiciones: {trans_min}")

print("\nCOMPARACIÓN FINAL")
print(f"AFD directo     -> Estados: {estados_directo}, Transiciones: {trans_directo}")
print(f"AFD minimizado  -> Estados: {estados_min}, Transiciones: {trans_min}")