class Estudiante:
    def __init__(self, nombre="", apellidos="", edad=0, sexo="", direccion="", carrera="", email="", telefono=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.carrera = carrera
        self.email = email
        self.telefono = telefono

    def imprimir_informacion(self):
        print("Información del Estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Carrera: {self.carrera}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")

estudiante = Estudiante(nombre="Maria", apellidos="Gonzalez", edad=21, sexo="Femenino", direccion="Avenida 456",
                                carrera="Ingeniería Informática", email="maria@example.com", telefono="8094278198")

estudiante.imprimir_informacion()