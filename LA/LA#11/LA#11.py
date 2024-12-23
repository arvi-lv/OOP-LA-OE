class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"Brand: {self.brand} \nModel: {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

iphone = Android("Iphone", "12 Max Wynn")
iphone.describePhone()