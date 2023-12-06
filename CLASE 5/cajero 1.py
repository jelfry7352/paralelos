class CajeroAutomatico:
    def __init__(self):
        self.cuentas = {'usuario1': {'pin': 3389, 'saldo': 1000000},
                        'usuario2': {'pin': 1525, 'saldo': 1500000}}

    def validar_usuario(self, usuario, pin):
        if usuario in self.cuentas and self.cuentas[usuario]['pin'] == pin:
            return True
        else:
            return False

    def consultar_saldo(self, usuario):
        return self.cuentas[usuario]['saldo']

    def retirar_dinero(self, usuario, monto):
        if monto > 0 and monto <= self.cuentas[usuario]['saldo']:
            self.cuentas[usuario]['saldo'] -= monto
            return True
        else:
            return False


cajero = CajeroAutomatico()

usuario = input("Ingrese su usuario: ")
pin = int(input("Ingrese su PIN: "))

if cajero.validar_usuario(usuario, pin):
    print(f"Bienvenido, {usuario}.\nSeleccione una opción:")
    print("1. Consultar saldo\n2. Retirar dinero")

    opcion = int(input())

    if opcion == 1:
        saldo = cajero.consultar_saldo(usuario)
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == 2:
        monto = int(input("Ingrese el monto a retirar: "))
        if cajero.retirar_dinero(usuario, monto):
            print(f"Retiro exitoso. Su saldo actual es: ${cajero.consultar_saldo(usuario)}")
        else:
            print("Fondos insuficientes o monto inválido.")
    else:
        print("Opción no válida.")
else:
    print("Usuario o PIN incorrecto.")