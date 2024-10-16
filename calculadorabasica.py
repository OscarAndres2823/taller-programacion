# Solicita al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Solicita al usuario que ingrese una operación matemática
operacion = input("Ingresa una operación (+, -, *, /): ")

# Usa match para realizar la operación correspondiente
match operacion:
    case "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Operación no válida.")
        