# Solicita al usuario el número de horas de estacionamiento
horas = float(input("Ingresa el número de horas de estacionamiento: "))

# Calcula el costo basado en las tarifas progresivas
if horas <= 1:
    costo = 5
elif horas <= 4:
    costo = 5 + (horas - 1) * 4
else:
    costo = 5 + 3 * 3 + (horas - 4) * 3

# Muestra el costo total de estacionamiento
print(f"El costo total de estacionamiento es: ${costo:.2f}")
