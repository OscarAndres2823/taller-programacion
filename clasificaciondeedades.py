# Solicita al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Clasifica a la persona según la edad
if edad >= 0 and edad <= 12:
    print("Eres un niño.")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un anciano.")
else:
    print("Edad no válida.")
