# Solicita al usuario un número entero positivo
n = int(input("Ingresa un número entero positivo: "))

# Verifica que el número ingresado sea positivo
if n <= 0:
    print("Por favor, ingresa un número entero positivo mayor que 0.")
else:
    # Inicializa la variable para la suma
    suma = 0
    
    # Usa un ciclo for para sumar los primeros n números enteros
    for i in range(1, n + 1):
        suma += i
    
    # Muestra el resultado
    print(f"La suma de los primeros {n} números enteros es: {suma}")
