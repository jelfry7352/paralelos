class Persona:
    def __init__(self, nombre="", apellidos="", edad=0, sexo="", direccion=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion

    def imprimir_informacion(self):
        print("Información de la Persona:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")

persona1 = Persona(nombre="Jelfry", apellidos="Pérez", edad=24, sexo="Masculino", direccion="Calle Principal")

persona1.imprimir_informacion()