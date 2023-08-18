def mayor (a, b):
    if a > b :
        print('"a" es mayor a "b"')
    else:
        print('"b" es mayor a "a"')

mayor(9, 8)
mayor(9, 10)

def potenciacion (base, exponente):
    return print(base ** exponente)

potenciacion(exponente=5, base=3) #Si defino las variables de los argumentos, el orden de los mismos es indiferente

def valor_por_defecto(base, exponente = 2): #Si el user no define el argumento, el programa va a buscar el seteado
    return print(base ** exponente)

valor_por_defecto(8)
valor_por_defecto(8, exponente=3)
valor_por_defecto(8, 3)

#Funciones Lambda --> Funciones estructuradas en una sola linea de codigo, primera parte argumentos, segunda el return
potenciacion_lambda = lambda base, exponente: print(base ** exponente)
potenciacion_lambda(3, 4)

def potenciacion_con_help (base, exponente):
    """
    Funcion para calcular la potencia de un numero
    """
    return print(base ** exponente)
help(potenciacion_con_help)