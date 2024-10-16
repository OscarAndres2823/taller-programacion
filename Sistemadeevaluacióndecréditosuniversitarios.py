# Solicita al usuario el número de materias cursadas
numero_materias = int(input("Ingresa el número de materias cursadas: "))

# Inicializa el contador de créditos
creditos_totales = 0

# Recorre cada materia para solicitar el puntaje y determinar si ha sido aprobada
for i in range(numero_materias):
    # Solicita el puntaje para cada materia
    puntaje = float(input(f"Ingresa el puntaje obtenido en la materia {i + 1}: "))
    
    # Determina si el puntaje es aprobado (>= 60) o no
    if puntaje >= 60:
        creditos_totales += 3  # Cada materia aprobada otorga 3 créditos

# Muestra el número total de créditos obtenidos
print(f"El número total de créditos obtenidos es: {creditos_totales}")
