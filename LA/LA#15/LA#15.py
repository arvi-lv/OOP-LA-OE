class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Sabi ni {self.name} ay Arf")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Sabi ni {self.name}ay Mau")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Sabi ni {self.name} ay ahha")


dog = Dog("Dwag")
cat = Cat("Mikmik")
bird = Bird("??")

def animal_sounds(animals):
    animal.speak()

animals = [dog, cat, bird]
for animal in animals:
    animal.speak()