class calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

        self.suma = 0
        self.resta = 0
        self.multiplicacion = 0
        self.division = 0

    def sumar(self):
        self.suma = self.numero1 + self.numero2
        print(f"la suma de {self.numero1} y {self.numero2} es: {self.suma}")

    def restar(self):
        self.resta = self.numero1 - self.numero2
        print(f"la resta de {self.numero1} y {self.numero2} es: {self.resta}")

    def multiplicar(self):
        self.multiplicacion = self.numero1 * self.numero2
        print(f"la multiplicacion de {self.numero1} y {self.numero2} es: {self.multiplicacion}")

    def dividir(self):
        if self.numero2 != 0:
            self.division = self.numero1 / self.numero2
            print(f"la division de {self.numero1} y {self.numero2} es: {self.division}")
        else:
            print("Error: No se puede dividir entre cero.")

calcular = calculadora(10, 5)
calcular.sumar()
calcular.restar()
calcular.multiplicar()
calcular.dividir()