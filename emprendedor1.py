
# Solicitar al usuario que ingrese el precio de suscripción
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))

# Solicitar al usuario que ingrese el número de usuarios
num_usuarios = int(input("Ingrese el número de usuarios: "))

# Solicitar al usuario que ingrese los gastos totales
gastos_totales = float(input("Ingrese los gastos totales: "))

# Formula calculo utilidades
utilidades = (precio_suscripcion * num_usuarios - gastos_totales)

# Mostrar resultado
print (f"Las utilidades del proyecto son {utilidades}")

