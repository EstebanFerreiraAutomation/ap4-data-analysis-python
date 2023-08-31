sueldos_Juan = {
    "Enero" : 300,
    "Febrero" : 300,
    "Marzo" : 300,
    "Abril" : 300,
    "Mayo" : 300,
    "Junio": 300,
    "Julio" : 500,
    "Agosto" : 500,
    "Septiembre": 500,
    "Octubre": 500,
    "Noviembre": 700,
    "Diciembre": 700
}

def calcular_sueldo_promedio(sueldo_anual):
    total = 0
    for sueldo in sueldo_anual:
        total = total+sueldo
    return total/12

sueldo_promedio_de_Juan = calcular_sueldo_promedio(sueldos_Juan.values())
print(f'El sueldo promedio de Juan es: {sueldo_promedio_de_Juan}')

if sueldo_promedio_de_Juan < 300:
    print('El sueldo de Juan es bajo')
elif sueldo_promedio_de_Juan >= 300 and sueldo_promedio_de_Juan <= 900:
    print('El sueldo de Juan es normal')
else:
    print('El sueldo de Juan es alto')