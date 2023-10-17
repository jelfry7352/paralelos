nota = int(input("Digite una opcion: "))

match nota:
    case 1:
        print("opcion A")
    case 2:
        print("opcion B")
    case 3:
        print("opcion C")
    case 4:
        print("opcion D")
    case 5:
        print("opcion F")
    case _:
        print("Seleccionar una opcion validad")