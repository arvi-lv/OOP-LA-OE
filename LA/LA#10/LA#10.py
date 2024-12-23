class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"Brand: {self.brand} \nModel: {self.model} \nFuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

mitsubishi = Car("Mitsubishi", "Montero Sport", "150 lang")
rusi = Motorcycle("Rusi", "Pang tatay", "50 lang")

mitsubishi.describeVehicle()
rusi.describeVehicle()