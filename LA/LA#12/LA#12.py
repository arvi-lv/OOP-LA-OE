class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describeToy(self):
        print(f"Name: {self.name} \nPrice: {self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

toy = Toy("Barbie", 2)
toy.describeToy()