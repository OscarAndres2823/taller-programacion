# Solicita al usuario la distancia a recorrer en kilómetros
distancia = float(input("Ingresa la distancia a recorrer en km: "))

# Solicita la velocidad promedio del automóvil en km/h
velocidad = float(input("Ingresa la velocidad promedio en km/h: "))

# Calcula el tiempo de viaje en horas
tiempo_viaje_horas = distancia / velocidad

# Convierte el tiempo a horas y minutos
horas = int(tiempo_viaje_horas)
minutos = int((tiempo_viaje_horas - horas) * 60)

# Muestra el tiempo de viaje en horas y minutos
print(f"El tiempo de viaje es de {horas} horas y {minutos} minutos.")

# Muestra un mensaje de advertencia si la velocidad es mayor a 120 km/h
if velocidad > 120:
    print("Advertencia: Estás superando la velocidad permitida de 120 km/h.")
