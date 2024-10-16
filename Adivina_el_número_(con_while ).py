import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print("He pensado en un número entre 1 y 100. Intenta adivinarlo.")

# Inicializa el intento del usuario
intento = None

# Usa un ciclo while para permitir al usuario seguir intentando
while intento != numero_secreto:
    # Solicita al usuario que ingrese un número
    intento = int(input("Ingresa tu adivinanza: "))
    
    # Compara el intento con el número secreto y proporciona pistas
    if intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número secreto es menor. Intenta de nuevo.")
    else:
        print("¡Felicidades! ¡Has adivinado el número secreto!")

