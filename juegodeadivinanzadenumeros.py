import random

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializa la variable de la suposición del usuario
adivinanza = None

print("¡Adivina el número entre 1 y 10!")

# Bucle hasta que el usuario adivine correctamente
while adivinanza != numero_secreto:
    # Solicita al usuario que ingrese su adivinanza
    adivinanza = int(input("Ingresa tu adivinanza: "))

    # Compara la adivinanza con el número secreto
    if adivinanza < numero_secreto:
        print("El número es mayor.")
    elif adivinanza > numero_secreto:
        print("El número es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")
