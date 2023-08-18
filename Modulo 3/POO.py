class Persona:
    """
    Clase que pide todos los datos de una persona
    """
    def __init__(self, nombre, apellido, dni):
        #Cuando creamos una instancia, va a pedir todo lo que agreguemos en init (su constructor)
        self.nombre = nombre #El parámetro self se refiere al objeto instanciado 
        self.apellido = apellido #de esa clase sobre el cual se está invocando dicho método.
        self.dni = dni

#Creo un objeto (instancia de la clase) persona

esteban = Persona("Esteban", "Apellido", "12345678")
print(esteban.nombre)
print(esteban.apellido)
print(esteban.dni)
print(type(esteban))