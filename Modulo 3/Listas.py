my_list = list(["1", 2, "3"])
my_list2 = [1, "2", 3]
print(type(my_list[0]))
print(type(my_list[1]))

for item in my_list:
    print(type(item))
    print(item)

for item in my_list2:
    print(type(item))
    print(item)

my_list.append('Hello') # --> Va a agregar el nuevo elemento al final de la lista
print(my_list)

my_list.insert(2, 999) # --> Va a agregar el nuevo elemento en la posicion 2 de la lista
print(my_list)

my_list[2] = '3' # --> Devuelvo a la posicion 2 su valor original
print(my_list)
my_list.pop(3) # --> Elimino el elemento de la posicion 3 para que no se repita el valor devuelto
print(my_list)

my_list3 = my_list + my_list2 # --> Unir listas
print(my_list3)

my_list_x_5 = my_list * 5 # --> Imprimo 5 veces los elementos de la lista
print(my_list_x_5)

my_list_inverted = my_list[::-1] # --> Invertir lista
print(my_list_inverted)

my_int_list = [3, 1, 4, 2]
my_int_list.sort() # --> Ordena la lista en forma ascendente, solo funciona con numbers
print(my_int_list)
print(len(my_int_list)) # --> Imprime la longitud de elementos de mi lista, en este caso 4

my_int_list.clear() # --> Vaciar lista
print(my_int_list)
