class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describeAnimal(self):
        print(f"Name: {self.name} \nType: {self.type}")

class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.can_swim = True

isda = Fish("Bangus", "Fish")
print(isda.can_swim)