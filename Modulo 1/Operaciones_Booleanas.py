a = True
b = False

print(a and a) # True and True --> True
print(a and b) # True and False --> False
print(a or a) #True or True --> True
print(a or b) # True or False --> True
print(b or b) # False or False --> False

print((3<4) and (4<5)) # True
print((3<4) and (6<5)) # False

# Negacion --> not
resultado = a and a #T and T --> True
print(resultado) #True
print(not resultado) # negado -> False

