# Solicita al usuario una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Inicializa el contador de vocales
contador_vocales = 0

# Define un conjunto de vocales para verificar
vocales = "aeiou"

# Recorre cada carácter de la cadena
for caracter in cadena.lower():
    # Verifica si el carácter es una vocal
    if caracter in vocales:
        contador_vocales += 1

# Muestra el número total de vocales
print(f"La cadena de texto contiene {contador_vocales} vocales.")
