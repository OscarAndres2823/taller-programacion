# Solicita al usuario que ingrese una calificación
calificacion = int(input("Ingresa tu calificación: "))

# Determina si la calificación es aprobatoria o reprobatoria
if calificacion >= 60:
    print(f"Con una calificación de {calificacion}, has aprobado.")
else:
    print(f"Con una calificación de {calificacion}, has reprobado.")