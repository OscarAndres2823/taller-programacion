# Solicita al usuario los tres ángulos del triángulo
angulo1 = float(input("Ingresa el primer ángulo en grados: "))
angulo2 = float(input("Ingresa el segundo ángulo en grados: "))
angulo3 = float(input("Ingresa el tercer ángulo en grados: "))

# Verifica si la suma de los ángulos es igual a 180 grados (validación básica para triángulo)
if angulo1 + angulo2 + angulo3 != 180:
    print("Los ángulos ingresados no forman un triángulo válido.")
else:
    # Clasifica el triángulo según sus ángulos
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipo = "Rectángulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        tipo = "Obtuso"
    else:
        tipo = "Agudo"
    
    # Muestra el tipo de triángulo
    print(f"El triángulo es {tipo}.")

