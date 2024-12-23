class Car:
    def __init__ (self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"Brand: {self.brand} \nColor: {self.color}"
    
car = Car("Tesla", "Red")

print(car)
print(car)
del car
