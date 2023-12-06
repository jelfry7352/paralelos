class Alumno:
    #contenido de la clase

class Alumno:
    nombre="Jelfry"
    apellido="Batista"

    def NombreCompleto(self):
        return self.nombre+""+self.apellido
    
alu= Alumno()
alu.nombre=input("Nombre..:")
alu,apellido=input("Apellido..:")

print(alu.NombreCompleto())