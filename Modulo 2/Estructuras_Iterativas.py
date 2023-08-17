#Bucles

#while -> requiere método de corte porque si no es infinito

numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1 #si comento esta línea, es infinito porque la condición siempre es true

# Break

numero = 1
while numero < 10:
    if numero == 5:
        break

    print(numero)
    numero = numero + 1

# For -> por cada valor del array ejecuto el bloque de código

gustos_manuchao = ["los aviones", "viajar", "la mañana", "el viento", "soñar", "la mar"]

for gusto in gustos_manuchao:
    print(f"Me gusta {gusto}, me gustas tú")

# Rango -> Genera sequencia de números en rango de valores que yo defina, valor del medio igual al límite

for numero in range(1, 20, 3):
    print(numero)