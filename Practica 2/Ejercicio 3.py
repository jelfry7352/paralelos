class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Monto no válido o insuficiente saldo.")

    def calcular_interes(self, tasa_interes):
        interes = self.saldo * (tasa_interes / 100)
        self.depositar(interes)
        print(f"Interés calculado y depositado. Nuevo saldo: ${self.saldo}")

    def imprimir_informacion(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo}")



cuenta = CuentaBancaria(numero_cuenta="123456789", titular="Jelfry Pérez", saldo=1000.0)

cuenta.imprimir_informacion()

cuenta.depositar(500.0)

cuenta.retirar(200.0)

cuenta.calcular_interes(2.5)

cuenta.imprimir_informacion()