def suma_try(num1, num2):
    try:
        print(int(num1) + int(num2))
    except:
        print("Ha ocurrido un error al sumar")

n1 = "texto"
n2= 2

suma_try(n1, n2)