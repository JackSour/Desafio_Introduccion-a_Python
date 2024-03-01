
import math

# Solicitar al usuario que ingrese el radio en kilómetros
radio_km = float(input("Ingrese el radio en Kilómetros: "))

# Convertir el radio de kilómetros a metros
radio_m = radio_km * 1000

# Solicitar al usuario que ingrese la constante gravitacional
constante_g = float(input("Ingrese la constante g: "))

# Calcular la velocidad de escape utilizando la fórmula
velocidad_escape = math.sqrt(2 * constante_g * radio_m)

# Mostrar la velocidad de escape calculada
print("La velocidad de Escape es {:.1f} [m/s]".format(velocidad_escape))

