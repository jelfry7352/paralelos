class Persona:
    def __init__(self, nombre="", apellidos="", edad=0, sexo="", direccion="", email="", sueldo=0.0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.email = email
        self.sueldo = sueldo

    def asignar_sueldo(self, sueldo):
        self.sueldo = sueldo

    def calcular_afp(self):
       
        return 0.1 * self.sueldo  
    def calcular_ars(self):
        return 0.05 * self.sueldo  
    def calcular_irs(self):
        return 0.15 * self.sueldo 
    def imprimir_informacion(self):
        print("Información de la Persona:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Email: {self.email}")
        print(f"Sueldo: {self.sueldo}")
        print(f"AFP: {self.calcular_afp()}")
        print(f"ARS: {self.calcular_ars()}")
        print(f"IRS: {self.calcular_irs()}")


persona1 = Persona(nombre="Jelfry", apellidos="Pérez", edad=24, sexo="Masculino", direccion="Calle Principal",
                          email="jelfry@example.com", sueldo=500000)

persona1.asignar_sueldo(600000)

persona1.imprimir_informacion()