class vehicle:
    def __init__(self, brand, color, plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0

    def acelerar(self):
        self.speed += 10
        print(f"el {self.brand} con placa {self.plate} acelero a {self.speed} km/h")

    def desacelerar(self):
            self.speed = self.speed - 10
            print(f"el {self.brand} con placa {self.plate} desacelero a {self.speed} km/h")
    

my_vehicle = vehicle('ferrari', 'red', 'abc 123')
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.desacelerar()