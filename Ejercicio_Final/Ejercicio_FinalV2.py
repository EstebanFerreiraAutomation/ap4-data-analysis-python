meses = tuple(('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'))
sueldos = []
nombre = input("Ingrese su nombre: ")

for mes in meses:
    i = 0
    sueldos.insert(i, int(input(f"Ingrese el sueldo de {mes}: ")))
    i = i+1

def calcular_sueldo_promedio(sueldo_anual):
    total = 0
    for sueldo in sueldo_anual:
        total = total+sueldo
    return total/12

sueldo_promedio = calcular_sueldo_promedio(sueldos)
print(f'El sueldo promedio de {nombre} es: {sueldo_promedio}')

if sueldo_promedio < 300:
    print(f'El sueldo de {nombre} es bajo')
elif sueldo_promedio >= 300 and sueldo_promedio <= 900:
    print(f'El sueldo de {nombre} es medio')
else:
    print(f'El sueldo de {nombre} es alto')