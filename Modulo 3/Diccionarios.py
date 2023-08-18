my_dict = {
    "clave" : "valor",
    "Nombre" : "Esteban",
    "Apellido" : "Ferreira"
}

print(my_dict["Nombre"])
print(my_dict["Apellido"])
print(my_dict.get("Nombre"))
print(len(my_dict)) # Imprime la longitud de elementos de un diccionario

# Iterar en llaves
for key in my_dict.keys():
    print(key)

# Iterar en valores
for value in my_dict.values():
    print(value)

# Iterar en ítems
for key, value in my_dict.items():
    print(f'key {key}, value {value}')

print('Nombre' in my_dict) # Devuelve si la clave existe o no en el diccionario
print('DNI' in my_dict) #False, no existe la key