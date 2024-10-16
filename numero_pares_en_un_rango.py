# Solicita al usuario el valor de inicio y fin del rango
inicio = int(input("Ingresa el valor de inicio del rango: "))
fin = int(input("Ingresa el valor de fin del rango: "))

# Verifica que el valor de inicio sea menor o igual que el valor de fin
if inicio > fin:
    print("El valor de inicio debe ser menor o igual que el valor de fin.")
else:
    # Recorre el rango de números desde inicio hasta fin (inclusive)
    print("Números pares en el rango:")
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            print(numero)
