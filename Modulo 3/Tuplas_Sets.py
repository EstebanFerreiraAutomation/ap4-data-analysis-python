#Tuplas --> Como las listas pero inmutables, una especie de lista constante

my_tuple = tuple(('x', 'b', 'm', 'r'))
print(my_tuple[1])

#Sets o conjuntos --> similares a las listas, pero estas no permiten elementos repetidos e incluso si lo declaras 
# con valores repetidos, solo se guardará un valor único.

my_set = set([2, 3, 4, 5])
my_set.discard(1) # --> a diferencia de .remove() No arroja una excepción si no encuentra el elemento

my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2) # --> intersection combina ambos sets y devuelve los valores en comun
print(my_new_set)

my_new_set = my_set_1.union(my_set_2) # --> Une los sets sin repetir los valores en común

my_new_set = my_set_1.difference(my_set_2) # --> muestra las diferencias entre ambos sets

print(my_new_set)