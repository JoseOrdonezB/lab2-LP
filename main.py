from src.regex import preparar_regex
from src.afd_directo import construir_afd_directo
from src.minimizacion import minimizar_afd

regex = input("Ingrese la expresión regular: ")

regex_preparada, alfabeto = preparar_regex(regex)

afd = construir_afd_directo(regex_preparada, alfabeto)

afd_min = minimizar_afd(afd, alfabeto)

estados_directo = len(afd["estados"])
trans_directo = sum(len(v) for v in afd["transiciones"].values())

estados_min = len(afd_min["estados"])
trans_min = sum(len(v) for v in afd_min["transiciones"].values())

# expresión regular para probar: (a|b)*abb(a|b)*

print("RESULTADO DE MINIMIZACION")

print("\nAFD DIRECTO")
print("Estados:", estados_directo)
print("Transiciones:", trans_directo)

print("\nAFD MINIMIZADO")
print("Estados:", estados_min)
print("Transiciones:", trans_min)