class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Error: La cantidad a retirar debe ser mayor que cero y no puede exceder el saldo disponible.")

    def imprimir_saldo(self):
        print(f"El saldo actual de la cuenta {self.numero} es: {self.__saldo}")


cuenta1 = Cuenta("12345", 1000)
print(cuenta1.numero)
cuenta1.depositar(500)
print(cuenta1.imprimir_saldo())