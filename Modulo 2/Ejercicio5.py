suma = 0
continuar = True

while continuar:
    input_usuario = input("Ingrese un número ('exit' para terminar): ")

    if input_usuario == 'exit':
        continuar = False
    else:
        numero = int(input_usuario)
        suma = suma + numero
        print(f"La suma es {suma}")

print(f"La suma final es {suma}")