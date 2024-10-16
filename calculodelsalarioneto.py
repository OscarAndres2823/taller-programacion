# Solicita al usuario que ingrese su salario bruto
salario_bruto = float(input("Ingresa tu salario bruto: "))

# Solicita al usuario que ingrese su país de residencia
pais = input("Ingresa tu país de residencia (País A, País B, País C): ").upper()

# Usa match para aplicar los impuestos correspondientes
match pais:
    case "PAÍS A":
        impuesto = 0.20
    case "PAÍS B":
        impuesto = 0.15
    case "PAÍS C":
        impuesto = 0.10
    case _:
        impuesto = 0.25  # Aplica 25% si el país no está en la lista

# Calcula el salario neto después de impuestos
salario_neto = salario_bruto * (1 - impuesto)

# Muestra el salario neto
print(f"Tu salario neto después de impuestos es: {salario_neto:.2f}")
