class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Brand: {self.brand} \nModel: {self.model}")

class WashingMachine(Appliance):
    def operate(self):
        print("panglaba")

class Refrigerator(Appliance):
    def operate(self):
        print("pangpalamig")

class Microwave(Appliance):
    def operate(self):
        print("pangpainit")

machine = WashingMachine("Midea", "122")
ref = Refrigerator("Condura", "Ria")
micro = Microwave("Samsung", "Mouo")

appliances = [machine, ref, micro]

for appliance in appliances:
	appliance.operate()
	appliance.info()