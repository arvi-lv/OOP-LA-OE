class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = Car("Tesla", "Black")
print(f"olor: {car.color}")

car.color = "White"

print(f"Updated color: {car.color}")