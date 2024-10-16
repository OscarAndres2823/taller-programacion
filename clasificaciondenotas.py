# Solicita al usuario que ingrese una nota numérica
nota = float(input("Ingresa una nota numérica: "))

# Clasifica la nota en función de su valor
if nota >= 90 and nota <= 100:
    print("Calificación: A")
elif nota >= 80 and nota < 90:
    print("Calificación: B")
elif nota >= 70 and nota < 80:
    print("Calificación: C")
elif nota >= 60 and nota < 70:
    print("Calificación: D")
elif nota < 60:
    print("Calificación: F")
else:
    print("Nota no válida.")
