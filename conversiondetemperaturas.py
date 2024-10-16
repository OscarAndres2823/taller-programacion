# Solicita al usuario que ingrese una temperatura
temperatura = float(input("Ingresa la temperatura: "))

# Solicita la escala de la temperatura (C para Celsius o F para Fahrenheit)
escala = input("Ingresa la escala (C para Celsius o F para Fahrenheit): ").upper()

# Usa match para convertir la temperatura a la escala opuesta
match escala:
    case "C":
        # Convierte de Celsius a Fahrenheit
        fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura}°C son {fahrenheit}°F.")
    case "F":
        # Convierte de Fahrenheit a Celsius
        celsius = (temperatura - 32) * 5/9
        print(f"{temperatura}°F son {celsius}°C.")
    case _:
        # En caso de una escala no válida
        print("Escala no válida. Ingresa 'C' para Celsius o 'F' para Fahrenheit.")
