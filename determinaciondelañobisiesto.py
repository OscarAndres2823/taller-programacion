# Solicita al usuario que ingrese un año
anio = int(input("Ingresa un año: "))

# Determina si el año es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
