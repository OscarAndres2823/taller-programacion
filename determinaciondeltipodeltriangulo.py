# Solicita al usuario que ingrese las longitudes de los tres lados del triángulo
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Verifica si los lados forman un triángulo válido
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    
    # Determina el tipo de triángulo
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero (todos los lados son iguales).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles (dos lados son iguales).")
    else:
        print("El triángulo es escaleno (todos los lados son diferentes).")
else:
    print("Las longitudes ingresadas no forman un triángulo válido.")
