# Solicita al usuario su peso en kilogramos
peso = float(input("Ingresa tu peso en kg: "))

# Solicita al usuario su altura en metros
altura = float(input("Ingresa tu altura en metros: "))

# Calcula el IMC
imc = peso / (altura ** 2)

# Muestra el IMC calculado
print(f"Tu IMC es: {imc:.2f}")

# Clasifica el estado de peso según el IMC
if imc < 18.5:
    print("Estado de peso: Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Estado de peso: Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Estado de peso: Sobrepeso")
else:
    print("Estado de peso: Obesidad")
