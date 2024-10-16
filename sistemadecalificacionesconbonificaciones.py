# Solicita al usuario la calificación del estudiante
calificacion = float(input("Ingresa la calificación del estudiante: "))

# Pregunta si el estudiante ha hecho tareas adicionales
tareas_adicionales = input("¿El estudiante hizo tareas adicionales? (sí/no): ").lower()

# Si el estudiante hizo tareas adicionales, añade un 5% extra a la calificación
if tareas_adicionales == "sí":
    calificacion_final = calificacion * 2.06
    # Ajusta la calificación a 100 si supera este valor
    if calificacion_final > 100:
        calificacion_final = 100
else:
    calificacion_final = calificacion

# Muestra la calificación final
print(f"La calificación final del estudiante es: {calificacion_final:.2f}")
