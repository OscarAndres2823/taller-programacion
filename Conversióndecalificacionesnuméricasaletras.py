# Solicita al usuario una calificación numérica
calificacion = float(input("Ingresa la calificación numérica (0-100): "))

# Usa match para convertir la calificación a una letra
match calificacion:
    case calificacion if 90 <= calificacion <= 100:
        letra = "A"
    case calificacion if 80 <= calificacion < 90:
        letra = "B"
    case calificacion if 70 <= calificacion < 80:
        letra = "C"
    case calificacion if 60 <= calificacion < 70:
        letra = "D"
    case calificacion if 0 <= calificacion < 60:
        letra = "F"
    case _:
        letra = "Calificación fuera del rango permitido (0-100)."

# Muestra la calificación en letra
print(f"La calificación en letra es: {letra}")
