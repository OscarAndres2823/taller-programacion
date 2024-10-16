# Inicializa la suma de los números pares
suma = 0

print("Ingresa números enteros. El programa sumará los números pares y se detendrá si ingresas un número impar.")

# Usa un ciclo while para solicitar números indefinidamente
while True:
    # Solicita al usuario un número entero
    numero = int(input("Ingresa un número entero: "))
    
    # Verifica si el número es impar
    if numero % 2 != 0:
        print("Número impar ingresado. El programa se detendrá.")
        break
    
    # Suma el número si es par
    suma += numero

# Muestra la suma de los números pares
print(f"La suma de los números pares es: {suma}")
