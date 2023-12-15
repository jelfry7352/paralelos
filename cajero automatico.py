class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero, saldo, limite_credito, tipo):
        self.numero = numero
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo = tipo

    def retirar_efectivo(self, cantidad):
        if self.saldo - cantidad >= -self.limite_credito:
            self.saldo -= cantidad
            return True
        else:
            return False

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def transferir_fondos(self, cuenta_destino, cantidad):
        if self.saldo - cantidad >= -self.limite_credito:
            self.saldo -= cantidad
            cuenta_destino.ingresar_efectivo(cantidad)
            return True
        else:
            return False

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta

class Cajero:
    def __init__(self, nombre, codigo, banco):
        self.nombre = nombre
        self.codigo = codigo
        self.banco = banco

    def retirar_efectivo(self, numero_cuenta, cantidad, contraseña):
        for cuenta in self.banco.cuentas:
            if cuenta.numero == numero_cuenta:
                if cuenta.retirar_efectivo(cantidad):
                    return f"Retirada exitosa. Nuevo saldo: {cuenta.saldo}"
                else:
                    return "Fondos insuficientes o límite de crédito excedido"
        return "Número de cuenta incorrecto"

    def ingresar_efectivo(self, numero_cuenta, cantidad, contraseña):
        for cuenta in self.banco.cuentas:
            if cuenta.numero == numero_cuenta:
                cuenta.ingresar_efectivo(cantidad)
                return f"Ingreso exitoso. Nuevo saldo: {cuenta.saldo}"
        return "Número de cuenta incorrecto"
    
    def transferir_fondos(self, numero_cuenta_origen, numero_cuenta_destino, cantidad, contraseña):
        cuenta_origen = None
        cuenta_destino = None

        for cuenta in self.banco.cuentas:
            if cuenta.numero == numero_cuenta_origen:
                cuenta_origen = cuenta
            elif cuenta.numero == numero_cuenta_destino:
                cuenta_destino = cuenta

        if cuenta_origen and cuenta_destino:
            if cuenta_origen.transferir_fondos(cuenta_destino, cantidad):
                return f"Transferencia exitosa. Nuevo saldo: {cuenta_origen.saldo}"
            else:
                return "Fondos insuficientes o límite de crédito excedido"
        else:
            return "Número de cuenta incorrecto"

# Ejemplo de uso:
banco = Banco("Mi Banco")
cliente1 = Cliente("Jelfry batista", "Calle Principal", "12345")
cliente2 = Cliente("Yoemely Dilone", "Calle Girasol", "67890")

cuenta1 = Cuenta("12345", 1000, 500, "Corriente")
cuenta2 = Cuenta("67890", 2000, 1000, "Ahorro")

banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)

cajero = Cajero("Cajero1", "123", banco)

print(cajero.retirar_efectivo("12345", 200, "contraseña"))
print(cajero.ingresar_efectivo("67890", 300, "contraseña"))
print(cajero.transferir_fondos("12345", "67890", 150, "contraseña"))
