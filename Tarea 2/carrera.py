carrera = ["ISC","INF"]
nombre = input("Carrera Seleccionada")
if nombre.upper() in carrera:
    print("Carrera Dispponible")
else:
    print("Carrera no disponible en este recinto")