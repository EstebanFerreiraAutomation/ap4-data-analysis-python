nro_1 = int(input("Ingrese un número entero: "))
nro_2 = int(input("Ingrese otro número entero: "))

if nro_1 < nro_2:
    print(str(nro_1) + " es menor que " + str(nro_2))
elif nro_1 > nro_2:
    print(str(nro_1) + " es mayor que " + str(nro_2))
else:
    print("Los números ingresados son iguales")